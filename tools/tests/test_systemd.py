import unittest
from pathlib import Path


class SystemdTests(unittest.TestCase):
    def test_timer_runs_at_ten_pm_chicago_and_catches_up(self):
        timer = Path("tools/systemd/math-notes-publisher.timer").read_text()
        self.assertIn("OnCalendar=*-*-* 22:00:00 America/Chicago", timer)
        self.assertIn("Persistent=true", timer)

    def test_service_reads_only_configured_vault_folders(self):
        service = Path("tools/systemd/math-notes-publisher.service").read_text()
        self.assertIn("tools/publish.py", service)
        self.assertIn(
            "--math-dir /home/monzo/Documents/Obsidian/Documents/Math",
            service,
        )
        self.assertIn(
            "--images-dir /home/monzo/Documents/Obsidian/Documents/Images",
            service,
        )


if __name__ == "__main__":
    unittest.main()
