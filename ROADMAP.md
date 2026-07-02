# Roadmap

## v0.1 — Foundation

- Establish core backend architecture with Clean Architecture principles.
- Implement the `Activity` and `Account` models with SQLAlchemy and PostgreSQL support.
- Expose REST API endpoints for creating, reading, updating, and deleting activities.
- Provide API documentation through OpenAPI and FastAPI automatic docs.
- Add Docker support for local development and deployment.

## v0.2 — Validation and Resilience

- Add input validation rules and service-level safeguards.
- Improve error handling and HTTP response consistency.
- Implement repository-level test coverage for core CRUD operations.
- Add database migration support and schema versioning.

## v0.3 — Security and Access Control

- Add authentication and authorization support for account management.
- Introduce secure password handling and account lifecycle policies.
- Enforce role-based access rules for activity operations.
- Harden API surface against common security threats.

## v0.5 — Integration and Observability

- Add request logging, structured diagnostics, and health endpoints.
- Support cross-service integration patterns such as webhooks or event publishing.
- Add metrics collection for request performance and database health.
- Improve documentation, example workflows, and onboarding guides.

## v1.0 — Production Readiness

- Deliver stable API contract and strong backward compatibility guarantees.
- Complete end-to-end integration tests and deployment pipelines.
- Publish production-grade Docker Compose configuration and deployment manifests.
- Establish contribution guidelines, release process, and community onboarding.
- Ensure the project is ready for broad usage and future extension.
