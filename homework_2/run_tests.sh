#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [[ ! -x "$ROOT_DIR/.venv/bin/python" ]]; then
  echo "Virtual environment not found. Run ./setup.sh first."
  exit 1
fi

cd "$ROOT_DIR"
"$ROOT_DIR/.venv/bin/python" -m pytest -q
