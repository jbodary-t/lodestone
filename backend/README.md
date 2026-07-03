# Lodestone Backend

This repository contains the Lodestone backend API built with FastAPI, SQLAlchemy, and PostgreSQL.

## Development

From the repository root, run the included centralized startup script:

PowerShell:

```powershell
.\scripts\dev.ps1
```

macOS / Linux:

```bash
./scripts/dev.sh
```

This script creates or updates the Python virtual environment, installs backend and frontend dependencies, and starts the backend and frontend development servers.

Open the API documentation at `http://127.0.0.1:8000/docs`.

## Docker

Run the backend with Docker Compose:

```bash
cd backend
docker compose up --build
```

The API will be available at `http://localhost:8000`.
