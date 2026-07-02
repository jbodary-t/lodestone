# Lodestone Coding Standards

## Python Standards

- Use clear and explicit imports.
- Prefer package-relative imports inside the backend package.
- Avoid rewriting imports with regex or automated scripts.
- Keep functions and classes small and well-scoped.
- Use type hints consistently where meaningful.
- Favor readability over cleverness.

## Pydantic and SQLAlchemy

- Use Pydantic v2 conventions.
- Replace `orm_mode` with `from_attributes` in Pydantic model configuration.
- Keep SQLAlchemy model columns explicit and typed.
- Do not mix unrelated concerns in model definitions.

## Configuration

- Support both local and Docker development.
- Use environment variables and `.env` files for runtime configuration.
- Do not hardcode service hostnames or credentials.
- Use SQLite as the default local development database when PostgreSQL is not available.

## Frontend Conventions

- Keep API base URLs configurable via environment variables.
- Document frontend/backend interaction clearly.

## Formatting and Readability

- Keep markdown documentation concise and actionable.
- Use consistent naming and file structure.
- Prefer simple, maintainable code.
