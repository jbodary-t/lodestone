# lodestone
Open-source progression optimization for RuneScape. Data-driven. Explainable. Built for Ironmen.

## Local Development

Use the included repository-level scripts to start the backend and frontend together.

PowerShell:

```powershell
.\scripts\dev.ps1
```

macOS / Linux:

```bash
./scripts/dev.sh
```

## Environment

The backend loads `backend/.env` and the frontend loads `frontend/.env` when available.

- `backend/.env.example`: required backend variables.
- `frontend/.env.example`: frontend runtime configuration.
