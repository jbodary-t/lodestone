# Lodestone Development Workflow

## Step-by-Step Process

1. Read relevant documentation.
2. Inspect the relevant code and package structure.
3. Determine the root cause of the issue.
4. Plan the smallest correct solution.
5. Implement the fix.
6. Start the application.
7. Fix the next failure.
8. Repeat until the objective is complete.

## Verification

- Do not stop after solving a single issue.
- Verify backend startup, frontend startup, database initialization, health endpoints, and integration paths.
- Confirm Swagger and frontend-backend communication after changes.

## When to Escalate

- If a human architectural decision is required, stop and explain the tradeoff.
- If the repository documentation conflicts with the chosen implementation, document the conflict.

## Developer-Friendly Outcome

- Preserve working software.
- Keep changes small and reviewable.
- Improve configuration clarity.
- Keep the codebase easier for future contributors to understand and extend.
