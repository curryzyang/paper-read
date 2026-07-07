#!/usr/bin/env bash
set -euo pipefail

HOST="${PREVIEW_HOST:-127.0.0.1}"
PORT="${1:-8010}"
OPEN_BROWSER="${PREVIEW_OPEN_BROWSER:-1}"

usage() {
  cat <<'EOF'
Usage:
  ./scripts/preview.sh [PORT]

Environment variables:
  PREVIEW_HOST         Server bind host (default: 127.0.0.1)
  PREVIEW_OPEN_BROWSER  0/1 to skip auto-open (default: 1)
EOF
}

if [[ "${1:-}" == "-h" || "${1:-}" == "--help" ]]; then
  usage
  exit 0
fi

if ! [[ "$PORT" =~ ^[0-9]{1,5}$ ]]; then
  echo "Error: PORT must be a valid number, got: $PORT"
  usage
  exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
cd "$PROJECT_ROOT"

if command -v python3 >/dev/null 2>&1; then
  PYTHON_BIN="python3"
elif command -v python >/dev/null 2>&1; then
  PYTHON_BIN="python"
else
  echo "Error: python/python3 is required but not found in PATH"
  exit 1
fi

URL="http://${HOST}:${PORT}/"
LOG_FILE="/tmp/daily-paper-preview-${PORT}.log"

echo "Preview: start server at ${URL}"

"${PYTHON_BIN}" -m http.server "$PORT" --bind "$HOST" >"${LOG_FILE}" 2>&1 &
SERVER_PID=$!

cleanup() {
  if kill -0 "${SERVER_PID}" >/dev/null 2>&1; then
    echo "Stopping preview server (pid=${SERVER_PID})"
    kill "${SERVER_PID}" >/dev/null 2>&1 || true
  fi
}
trap cleanup EXIT INT TERM

sleep 1
if ! kill -0 "${SERVER_PID}" >/dev/null 2>&1; then
  echo "Failed to start preview server. See ${LOG_FILE}"
  echo "---"
  cat "${LOG_FILE}"
  exit 1
fi

if [[ "${OPEN_BROWSER}" == "1" ]]; then
  if command -v open >/dev/null 2>&1; then
    open "$URL"
  elif command -v xdg-open >/dev/null 2>&1; then
    xdg-open "$URL" >/dev/null 2>&1 || true
  elif command -v explorer >/dev/null 2>&1; then
    explorer "$URL" >/dev/null 2>&1 || true
  fi
fi

echo "Preview is running at: ${URL}"
echo "Press Ctrl+C to stop."

wait "${SERVER_PID}"
