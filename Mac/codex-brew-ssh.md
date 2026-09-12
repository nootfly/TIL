You can clear the prompt remotely through SSH. I confirmed your Codex executable has macOS’s quarantine marker.

For the current installation, run:

```bash
xattr -d com.apple.quarantine /usr/local/bin/codex
codex --version
```

For future remote upgrades, run:

```bash
brew upgrade --cask codex &&
if xattr /usr/local/bin/codex | grep -qx 'com.apple.quarantine'; then
  xattr -d com.apple.quarantine /usr/local/bin/codex
fi
codex --version
```

This removes the downloaded-file confirmation for that Codex executable only. Use it for the trusted Codex package you intentionally installed.