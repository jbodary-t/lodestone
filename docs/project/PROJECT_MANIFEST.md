# Lodestone Project Manifest

## Vision

Lodestone is an open-source progression optimization platform for RuneScape. It is not a wiki, a quest helper, or a checklist generator. Lodestone is a decision engine that turns game facts into strategic recommendations.

The first supported journey is:
- Fresh RS3 Ironman → Trimmed Completionist Cape

Supported game lines:
- RuneScape 3
- Old School RuneScape

## Core Principles

- Everything is an Activity.
- Everything must be data-driven.
- Atlas stores facts.
- Navigator computes strategy.
- Never hardcode RuneScape logic.
- Support Ironman first.
- No microtransaction assumptions.
- Every recommendation must explain WHY.
- Recommendations should eventually include:
  - confidence
  - opportunity cost
  - estimated time saved
  - future unlock value
  - travel savings
  - resource impact

## Architecture

Lodestone is built around a clean separation of concerns:

- Atlas: canonical factual data stores, game data, and provider ingestion.
- Navigator: recommendation and optimization engine.
- Advisor: domain orchestration and activity lifecycle management.
- Forecast: runtime configuration, environment settings, and external dependency integration.
- Journey: end-to-end progression flows, from chosen goal to actionable next steps.

The current repository is structured as:
- `backend/app/core`: runtime configuration and environment settings.
- `backend/app/db`: database session management and base repositories.
- `backend/app/models`: domain entities and persistence mapping.
- `backend/app/schemas`: API contract definitions.
- `backend/app/api`: FastAPI request routing and endpoint exposure.
- `backend/app/services`: application services and business orchestration.
- `backend/app/repositories`: persistence adapters and query abstractions.
- `backend/app/requirements`: domain requirement models and evaluation logic.

## Core Systems

Lodestone must evolve along distinct system boundaries:

- Activity Engine
- Requirement Engine
- Reward Engine
- Account Engine
- Atlas
- Navigator
- Forecast
- Journey
- Guide Generator
- Bank Advisor
- PvM Planner
- Achievement Planner
- XP Planner
- Resource Planner
- Transportation Planner

## System Dependency Graph

1. Atlas
   - Purpose: establish factual game data and provider ingestion.
   - Outputs: canonical activity definitions, skill information, quest metadata, item information, unlocks, and account imports.
2. Account Engine
   - Depends on Atlas.
   - Outputs account state, progression status, player inventory, and achievement progress.
3. Requirement Engine
   - Depends on Atlas and Account Engine.
   - Produces requirement satisfaction status and missing dependencies for an activity.
4. Reward Engine
   - Depends on Atlas and Activity Engine.
   - Produces outcome analysis and value estimates for activity completion.
5. Navigator
   - Depends on Requirement Engine, Reward Engine, Account Engine, and Atlas.
   - Produces prioritized recommendations with rationale and scoring.
6. Journey
   - Depends on Navigator and Account Engine.
   - Produces sequenced plans toward a chosen goal.
7. Guide Generator
   - Depends on Journey and Atlas.
   - Produces human-readable plans and explanations.

## Data Providers

Lodestone must support interchangeable providers without coupling business logic to any one source.

- Official RuneScape Wiki (Wiki Sync)
- RuneMetrics
- Manual Entry
- CSV Import
- Smart Capture (OCR)
- Future Official APIs
- Future Plugins

## Supported Platforms

- Windows
- macOS (Intel)
- macOS (Apple Silicon)
- Linux
- Web Browser

Future platform goals:
- mobile web
- native mobile
- desktop clients via Electron or PWA

## Project Requirements

- Cross-platform support across Windows, macOS, Linux, and web.
- Atlas stores facts and remains the source of truth for game data.
- Navigator computes strategy and never becomes a facts database.
- Everything is data-driven.
- Everything is an Activity.
- Ironman-first support and account-first progression modeling.
- Multiple data providers.
- Smart Capture support for account ingestion.
- RuneMetrics integration.
- Wiki Sync integration.
- Extensible plugin architecture for future providers and sources.
- Support for future official APIs.
- Every recommendation must explain WHY.
- Recommendations should eventually include confidence and estimated impact metrics.

## Build Order

1. Atlas foundation and provider abstraction.
2. Account Engine and account model.
3. Activity Engine and canonical activity model.
4. Requirement Engine.
5. Reward Engine.
6. Navigator recommendation engine.
7. Journey planning and goal definitions.
8. Smart Capture and provider integrations.
9. Guide generation and explainability.
10. Platform-specific refinements and web frontend integration.

## Future Expansion

- Goal definitions for Quest Cape, Master Quest Cape, Completionist Cape, Trimmed Completionist Cape.
- Planner modules for PvM, achievements, resources, and transport.
- Smart capture pipelines for bank, equipment, boss log, achievements, collections, diaries, player-owned farm, and ports.
- Confidence modeling, time-saved estimates, and opportunity-cost scoring.
- Modular provider adapters and plugin ecosystem.
- Multi-account / multiplayer goal coordination.
- Offline-first and sync-capable experiences.
