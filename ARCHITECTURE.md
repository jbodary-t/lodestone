# Architecture

## Overview

Lodestone is structured around a clean architectural pattern that separates domain logic from infrastructure and delivery. The repository delineates backend services, data models, and API boundaries to keep the system maintainable, testable, and adaptable.

## Core Components

### Atlas

Atlas is the data layer of Lodestone. It defines the canonical persistence model and maps domain concepts to the database using SQLAlchemy. Atlas is responsible for database connectivity, migrations, and schema stability.

### Navigator

Navigator is the request-handling layer. It manages routing, HTTP election, and API versioning. Navigator translates external client requests into service actions and ensures API semantics remain consistent.

### Advisor

Advisor is the domain service layer. It encapsulates business rules, validation, and application workflows to keep domain logic independent of persistence and transport mechanisms.

### Forecast

Forecast is the configuration and runtime behavior boundary. It controls environment settings, database connections, and external dependency configuration while preserving a clear application surface.

### Journey

Journey represents the end-to-end flow of a request from API intake through validation, service orchestration, repository interaction, and response generation. Journey ensures that each path is traceable, composable, and aligned with domain intent.

## Backend Structure

The backend is organized into the following layers:

- `app/core`: Configuration, environment settings, and runtime constants.
- `app/db`: SQLAlchemy session management, repository base classes, and database initialization.
- `app/models`: Domain entities and database tables, including the core `Activity` and `Account` models.
- `app/schemas`: Pydantic schemas that define request and response contracts for the API.
- `app/api`: FastAPI routers and endpoint definitions that expose backend capabilities as RESTful services.
- `app/services`: Business logic services that orchestrate interactions between repositories and API handlers.
- `app/repositories`: Persistence adapters that encapsulate SQLAlchemy queries and CRUD operations.

## Activity Model

The `Activity` model is a first-class domain entity in Lodestone. It captures the essential state of a tracked item and includes:

- `title`: a concise name for the activity.
- `description`: optional longer text describing the activity.
- `owner_email`: the email identifier for the entity responsible for the activity.
- `status`: a lifecycle state such as `scheduled`, `in_progress`, or `completed`.
- `created_at` / `updated_at`: timestamps that support auditing and change tracking.

The model is intentionally simple so it can be extended safely while preserving the core behavior required for RESTful operations, validation, and lifecycle management.
