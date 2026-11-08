#!/usr/bin/env bash
# Mission Builds HQ | Mission 02: open the mission screen full screen on the cyberdeck.
# Press Alt+F4 to close it.
set -euo pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PAGE="file://${DIR}/index.html"

# Newer Raspberry Pi OS calls the browser "chromium"; older versions call it "chromium-browser".
BROWSER="$(command -v chromium || command -v chromium-browser || true)"
if [ -z "${BROWSER}" ]; then
  echo "Chromium wasn't found. Install it with: sudo apt install chromium" >&2
  exit 1
fi

exec "${BROWSER}" --kiosk --noerrdialogs --disable-session-crashed-bubble "${PAGE}"
