#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT_DIR"

if [[ ! -x "$ROOT_DIR/.venv/bin/python" ]]; then
  echo "Virtual environment not found. Run ./setup.sh first."
  exit 1
fi

source "$ROOT_DIR/.venv/bin/activate"
python -m pytest -q
