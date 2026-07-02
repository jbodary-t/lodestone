# Lodestone Backend

This repository contains the Lodestone backend API built with FastAPI, SQLAlchemy, and PostgreSQL.

## Development

1. Create a Python 3.12 virtual environment.
2. Install dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

3. Start the application:

   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

4. Open the API documentation at `http://localhost:8000/docs`.

## Docker

Run the backend with Docker Compose:

```bash
cd backend
docker compose up --build
```

The API will be available at `http://localhost:8000`.
