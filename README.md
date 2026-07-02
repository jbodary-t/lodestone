# lodestone
Open-source progression optimization for RuneScape. Data-driven. Explainable. Built for Ironmen.

## Local Development

Use the included scripts to start the backend and frontend together.

PowerShell:

```powershell
.\scripts\start-dev.ps1
```

macOS / Linux:

```bash
./scripts/start-dev.sh
```

## Environment

The backend loads `backend/.env` and the frontend loads `frontend/.env` when available.

- `backend/.env.example`: required backend variables.
- `frontend/.env.example`: frontend runtime configuration.
