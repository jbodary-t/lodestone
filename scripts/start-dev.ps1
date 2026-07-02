$ErrorActionPreference = 'Stop'

Write-Host "[lodestone] Verifying tooling..."

function Check-Command($name, $command) {
    try {
        Invoke-Expression $command | Out-Null
        Write-Host "[lodestone] Found $name"
        return $true
    } catch {
        Write-Host "[lodestone] Missing $name"
        return $false
    }
}

$pythonOk = Check-Command "Python" "python --version"
$nodeOk = Check-Command "Node" "node --version"
$npmOk = Check-Command "npm" "npm --version"

if (-not $pythonOk) { Write-Error "Python is required. Install Python 3.12+ and retry."; exit 1 }
if (-not $nodeOk) { Write-Error "Node.js is required. Install Node.js and retry."; exit 1 }
if (-not $npmOk) { Write-Error "npm is required. Install npm and retry."; exit 1 }

Write-Host "[lodestone] Preparing backend environment..."
if (-not (Test-Path ".venv")) {
    python -m venv .venv
}
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r backend\requirements.txt

Write-Host "[lodestone] Installing frontend dependencies..."
Push-Location frontend
npm install
Pop-Location

Write-Host "[lodestone] Starting backend and frontend..."
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd $PWD\backend; ..\.venv\Scripts\python.exe -m uvicorn app.main:app --host 0.0.0.0 --port 8000"
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd $PWD\frontend; npm run dev -- --hostname 0.0.0.0 --port 3000"
Write-Host "[lodestone] Backend: http://localhost:8000"
Write-Host "[lodestone] Frontend: http://localhost:3000"
