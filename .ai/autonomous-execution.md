# Autonomous Execution Policy

## Safe Actions

The AI may perform the following development actions without explicit confirmation:

- Start backend and frontend services locally.
- Install project dependencies in the local workspace environment.
- Create virtual environments for the project.
- Install npm and Python dependencies for the workspace.
- Update local project files and documentation.
- Create new project files and directories.
- Run tests, formatting, and linting.
- Build backend or frontend code.
- Run non-destructive migrations.
- Verify APIs and application startup.
- Manage environment variables within the current terminal session for debugging only.

## Environment Rules

- Temporary environment variable changes are allowed within the current terminal session.
- Never permanently modify user system environment variables without explicit approval.
- Prefer local session changes over permanent OS-level changes.

## Destructive Operations Requiring Approval

The AI must request approval before performing any of the following:

- Deleting files or directories.
- Moving or renaming packages.
- Bulk search-and-replace across the repository.
- Regex-based rewriting of project files.
- Resetting Git history.
- Force pushing changes.
- Deleting database data or dropping tables.
- Changing licenses or repository visibility.
- Installing global software or modifying OS settings.
- Making changes outside the current repository without approval.

## Verification Requirement

- After each meaningful change, run the application and confirm the next error or success state.
- Continue until the current objective is complete or a human architectural decision is required.
