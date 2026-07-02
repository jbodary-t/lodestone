#!/usr/bin/env bash
set -e

echo "[lodestone] Verifying tooling..."

command -v python >/dev/null 2>&1 || { echo "Python is required. Install Python 3.12+ and retry."; exit 1; }
command -v node >/dev/null 2>&1 || { echo "Node.js is required. Install Node.js and retry."; exit 1; }
command -v npm >/dev/null 2>&1 || { echo "npm is required. Install npm and retry."; exit 1; }

echo "[lodestone] Preparing backend environment..."
if [ ! -d ".venv" ]; then
  python -m venv .venv
fi
. .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r backend/requirements.txt

echo "[lodestone] Installing frontend dependencies..."
cd frontend
npm install
cd ..

echo "[lodestone] Starting backend and frontend..."
. .venv/bin/activate
cd backend
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 &
cd ../frontend
npm run dev -- --hostname 0.0.0.0 --port 3000
