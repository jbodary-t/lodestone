# Lodestone Review Checklist

## Code Changes

- Is the change small and focused?
- Does it preserve existing behavior unless intentionally updated?
- Are imports explicit and package-aware?
- Are there no unnecessary mass edits or regex rewrites?

## Documentation

- Was the change documented in code comments or project docs?
- Are configuration changes reflected in `.env.example` or README files?
- Is the startup and developer experience clear?

## Architecture

- Does the change respect Lodestone's architecture and data-driven philosophy?
- Does it avoid hardcoding game logic?
- Does it support multiple account types and journey modes where relevant?

## Verification

- Has the backend been started successfully?
- Has the frontend been started successfully?
- Has the database initialization path been verified?
- Does the health endpoint work?
- Does Swagger load?
- Can the frontend communicate with the backend?

## Quality

- Are naming and conventions consistent?
- Are tests added or updated when needed?
- Is the change readable and maintainable?
- Does the change improve developer experience?
