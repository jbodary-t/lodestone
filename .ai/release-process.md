# Release Process

## Purpose

Document the standard process for releasing Lodestone updates.

## Release Steps

1. Confirm the local development environment is stable.
2. Run backend and frontend startup verification.
3. Run automated tests.
4. Update changelog or release notes if applicable.
5. Ensure documentation reflects any public-facing configuration changes.
6. Create a pull request with a clear summary and testing notes.
7. Review and merge with at least one additional reviewer.
8. Tag the release if appropriate.

## Versioning

- Follow semantic versioning for public releases.
- Use metadata or pre-release tags for work-in-progress builds.

## Deployment

- Production deployment should use containerized or managed infrastructure.
- Ensure environment variables are documented and secure.
- Preserve architecture and data integrity during deployment.
