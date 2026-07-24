import tempfile
import unittest
from pathlib import Path

from tools.publish import (
    build_publication,
    classify_note,
    sync_owned_output,
    validate_stage,
)


class ClassificationTests(unittest.TestCase):
    def test_quiz_and_multistep_override_subjects(self):
        self.assertEqual(classify_note("Quiz 2.md", "[[Algebra II]]"), "Quizzes")
        self.assertEqual(
            classify_note("Motion.md", "[[Multistep]] [[Calculus I]]"),
            "Quizzes",
        )
        self.assertEqual(
            classify_note("Limits.md", "Multi-step [[Algebra II]]"),
            "Quizzes",
        )

    def test_most_advanced_subject_wins(self):
        self.assertEqual(
            classify_note(
                "Mixed.md",
                "[[Algebra II]] [[Precalculus]] [[Calculus I]]",
            ),
            "Calculus I",
        )
        self.assertEqual(classify_note("Alias.md", "[[Calculus]]"), "Calculus I")

    def test_unclassified_note_is_skipped(self):
        self.assertIsNone(classify_note("Scratch.md", "[[Math Academy]]"))


class PublisherTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.math = self.root / "Math"
        self.images = self.root / "Images"
        self.stage = self.root / "stage"
        self.math.mkdir()
        self.images.mkdir()

    def tearDown(self):
        self.temporary.cleanup()

    def test_builds_sorted_notes_images_links_and_index(self):
        (self.math / "Derivative.md").write_text(
            "[[Calculus I]]\n"
            "![[Pasted image 1.png]]\n"
            "[[Linear Functions|linear review]]\n"
            "[[Unpublished Topic]]",
            encoding="utf-8",
        )
        (self.math / "Linear Functions.md").write_text(
            "[[Algebra II]]",
            encoding="utf-8",
        )
        (self.math / "Quiz 1.md").write_text(
            "[[Algebra II]]",
            encoding="utf-8",
        )
        (self.math / "Scratch.md").write_text(
            "[[Math Academy]]",
            encoding="utf-8",
        )
        (self.images / "Pasted image 1.png").write_bytes(b"png")
        (self.images / "private-photo.jpg").write_bytes(b"private")

        report = build_publication(self.math, self.images, self.stage)

        derivative = (self.stage / "Calculus I" / "Derivative.md").read_text()
        self.assertIn("![](../assets/Pasted%20image%201.png)", derivative)
        self.assertIn(
            "[linear review](../Algebra%20II/Linear%20Functions.md)",
            derivative,
        )
        self.assertIn("Unpublished Topic", derivative)
        self.assertNotIn("[[Unpublished Topic]]", derivative)
        self.assertTrue(
            (self.stage / "Algebra II" / "Linear Functions.md").is_file()
        )
        self.assertTrue((self.stage / "Quizzes" / "Quiz 1.md").is_file())
        self.assertEqual(
            (self.stage / "assets" / "Pasted image 1.png").read_bytes(),
            b"png",
        )
        self.assertFalse((self.stage / "assets" / "private-photo.jpg").exists())
        self.assertIn("Scratch.md", report.skipped)
        self.assertIn("Derivative", (self.stage / "README.md").read_text())
        validate_stage(self.stage)

    def test_rejects_unapproved_missing_and_symlinked_images(self):
        (self.math / "Images.md").write_text(
            "[[Calculus I]]\n"
            "![[private-photo.jpg]]\n"
            "![[Screenshot missing.png]]\n"
            "![[Pasted image link.png]]",
            encoding="utf-8",
        )
        (self.images / "private-photo.jpg").write_bytes(b"private")
        outside = self.root / "outside.png"
        outside.write_bytes(b"outside")
        (self.images / "Pasted image link.png").symlink_to(outside)

        report = build_publication(self.math, self.images, self.stage)

        self.assertEqual(tuple((self.stage / "assets").iterdir()), ())
        self.assertEqual(len(report.warnings), 3)

    def test_stage_rejects_unexpected_file_and_symlink(self):
        self.stage.mkdir()
        (self.stage / "secret.txt").write_text("no", encoding="utf-8")
        with self.assertRaises(ValueError):
            validate_stage(self.stage)
        (self.stage / "secret.txt").unlink()
        (self.stage / "assets").symlink_to(self.images)
        with self.assertRaises(ValueError):
            validate_stage(self.stage)

    def test_sync_replaces_owned_output_but_preserves_tools_and_git(self):
        repository = self.root / "repository"
        repository.mkdir()
        (repository / ".git").mkdir()
        (repository / "tools").mkdir()
        (repository / "tools" / "publish.py").write_text("preserve")
        (repository / "Calculus I").mkdir()
        (repository / "Calculus I" / "stale.md").write_text("stale")
        self.stage.mkdir()
        (self.stage / "README.md").write_text("new")
        for folder in (
            "Algebra II",
            "Precalculus",
            "Calculus I",
            "Quizzes",
            "assets",
        ):
            (self.stage / folder).mkdir()

        self.assertTrue(sync_owned_output(self.stage, repository))
        self.assertEqual((repository / "tools" / "publish.py").read_text(), "preserve")
        self.assertFalse((repository / "Calculus I" / "stale.md").exists())
        self.assertFalse(sync_owned_output(self.stage, repository))

    def test_sync_requires_git_checkout_and_rejects_owned_symlink(self):
        repository = self.root / "repository"
        repository.mkdir()
        self.stage.mkdir()
        (self.stage / "README.md").write_text("new")
        for folder in (
            "Algebra II",
            "Precalculus",
            "Calculus I",
            "Quizzes",
            "assets",
        ):
            (self.stage / folder).mkdir()
        with self.assertRaises(ValueError):
            sync_owned_output(self.stage, repository)
        (repository / ".git").mkdir()
        (repository / "assets").symlink_to(self.images)
        with self.assertRaises(ValueError):
            sync_owned_output(self.stage, repository)


if __name__ == "__main__":
    unittest.main()
