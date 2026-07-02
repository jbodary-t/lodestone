# Contributing to Lodestone

Thank you for contributing to Lodestone. This guide explains how to contribute code, file issues, and prepare pull requests for a professional open-source project.

## Coding Standards

- Use Python 3.12 features responsibly and maintain compatibility with the repository’s declared runtime.
- Follow PEP 8 formatting, meaningful naming, and small, focused functions.
- Keep domain logic in services, persistence details in repositories, and API handling in routers.
- Write clear docstrings for public functions and modules.
- Prefer explicit typing and Pydantic-based request/response validation.

## Commit Conventions

- Use present-tense summaries in commit messages.
- Prefix commit subjects with scope when appropriate, for example:
  - `api: add activity update endpoint`
  - `db: improve session management`
  - `docs: clarify architecture rationale`
- Include a short body when more context is needed.
- Keep each commit focused on a single change or improvement.

## Issue Workflow

- Open issues for bugs, enhancements, or architectural questions.
- Provide a concise summary, expected behavior, and reproduction steps.
- Link related issues or pull requests when applicable.
- Use labels to clarify the type of issue, such as `bug`, `enhancement`, or `discussion`.

## Pull Request Expectations

- Base pull requests on the `main` branch or the appropriate feature branch.
- Provide a clear description of the problem, the solution, and any relevant implementation details.
- Include test coverage or manual verification steps for all functional changes.
- Keep pull requests limited in scope to make reviews faster and safer.
- Address review comments promptly and update the branch with relevant fixes.

## Testing Requirements

- Add automated tests for new functionality and bug fixes.
- Ensure tests are deterministic and run cleanly in the repository environment.
- Include integration coverage for API endpoints where appropriate.
- Run the test suite before submitting any pull request.

## Documentation Standards

- Keep documentation accurate, concise, and up to date.
- Document new public APIs, configuration options, and architecture decisions.
- Use markdown files in the repository root for project-level guidance.
- Update related documentation when behavior or public interfaces change.
