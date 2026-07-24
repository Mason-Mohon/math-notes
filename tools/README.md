# Publisher

`publish.py` exports only classified Markdown files from the configured Math
directory and directly referenced screenshots with approved names from the
configured Images directory.

Preview everything that would become public:

```bash
python3 tools/publish.py \
  --math-dir /home/monzo/Documents/Obsidian/Documents/Math \
  --images-dir /home/monzo/Documents/Obsidian/Documents/Images \
  --dry-run
```

Run the tests:

```bash
python3 -m unittest discover -s tools/tests -v
```

Install the daily user timer:

```bash
install -D -m 0644 tools/systemd/math-notes-publisher.service \
  /home/monzo/.config/systemd/user/math-notes-publisher.service
install -D -m 0644 tools/systemd/math-notes-publisher.timer \
  /home/monzo/.config/systemd/user/math-notes-publisher.timer
systemctl --user daemon-reload
systemctl --user enable --now math-notes-publisher.timer
```

Inspect its schedule and logs:

```bash
systemctl --user list-timers math-notes-publisher.timer --all
journalctl --user -u math-notes-publisher.service -n 100 --no-pager
```

If a push fails after a local commit, retry it with:

```bash
git push origin HEAD
```
