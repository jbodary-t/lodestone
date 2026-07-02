# Lodestone Engineering Rules

## Change Discipline

- Make small, incremental changes.
- Keep commits and pull requests focused.
- Never remove unfinished systems simply because they are incomplete.
- Preserve working software at all times.
- Avoid wholesale package or architecture rewrites without explicit approval.

## Architecture

- Maintain the distinction between data, strategy, and presentation.
- Do not hardcode RuneScape rules in application logic.
- Prefer data-driven rules and provider-based configuration.
- Design for multiple account types and journey types from the start.
- Avoid assumptions about a single game mode, single journey, or single provider.

## Imports and Packaging

- Inspect package structure before editing imports.
- Use explicit package-relative imports within the backend package.
- Do not rewrite imports with mass regex or automated scripts.
- Keep import paths readable and maintainable.

## Environment and Configuration

- Support local development without Docker by default.
- Use SQLite as the default local development database.
- Preserve Docker/PostgreSQL support through environment configuration.
- Never hardcode Docker hostnames in the application.
- Use environment variables and `.env` files for runtime configuration.

## Pydantic and Models

- Use Pydantic v2 conventions.
- Replace `orm_mode` with `from_attributes` where appropriate.
- Keep SQLAlchemy and Pydantic model definitions explicit and maintainable.

## Developer Experience

- Improve setup commands and documentation when possible.
- Prefer cross-platform solutions.
- Document how to start backend and frontend locally.
- Keep developer-facing scripts simple and robust.
