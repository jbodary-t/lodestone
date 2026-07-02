# Lodestone Feature Matrix

This matrix describes planned user-facing features and their priority for the engineering foundation.

## Activity Management

- Purpose: enable users to define, view, and manage activities across RuneScape progression.
- Dependencies: Activity Engine, Atlas, API layer.
- Priority: High
- Version: v0.1
- Current Status: partial backend support; activity schema and basic CRUD exist.

## Account Management

- Purpose: manage player accounts, credentials, and progress state.
- Dependencies: Account Engine, API layer.
- Priority: High
- Version: v0.1
- Current Status: backend account model and basic create/read endpoints exist.

## Provider Selection

- Purpose: allow users to select and configure data providers for account ingestion.
- Dependencies: Data Providers, Atlas.
- Priority: High
- Version: v0.2
- Current Status: no provider UI or provider abstraction implemented yet.

## Goal Setup

- Purpose: let users choose game mode, goal type, and optimization target during first-run.
- Dependencies: Goal definitions, Journey.
- Priority: High
- Version: v0.2
- Current Status: planned; not yet implemented.

## Requirement Evaluation

- Purpose: determine whether an activity can be completed given account progress.
- Dependencies: Requirement Engine, Account Engine, Activity Engine.
- Priority: High
- Version: v0.2
- Current Status: requirement model skeleton exists; evaluator needs completion and integration.

## Recommendation Engine

- Purpose: generate ranked next-step recommendations with rationale.
- Dependencies: Navigator, Requirement Engine, Reward Engine, Account Engine.
- Priority: High
- Version: v0.3
- Current Status: simple recommendation stub exists.

## Journey Planner

- Purpose: create sequenced progression plans toward chosen goals.
- Dependencies: Navigator, Account Engine.
- Priority: High
- Version: v0.4
- Current Status: conceptual only.

## Smart Capture Import

- Purpose: ingest account state from screenshots, OCR, and capture pipelines.
- Dependencies: Smart Capture, Account Engine.
- Priority: Medium
- Version: v0.5
- Current Status: not implemented.

## Wiki Sync

- Purpose: synchronize RuneScape facts from official or community sources.
- Dependencies: Atlas, Data Providers.
- Priority: Medium
- Version: v0.5
- Current Status: not implemented.

## RuneMetrics Integration

- Purpose: import account progress from RuneMetrics.
- Dependencies: Data Providers, Account Engine.
- Priority: Medium
- Version: v0.5
- Current Status: not implemented.

## Resource Planning

- Purpose: model resource requirements and advise item management.
- Dependencies: Resource Planner, Bank Advisor, Atlas.
- Priority: Medium
- Version: v0.6
- Current Status: not implemented.

## Travel Optimization

- Purpose: recommend travel unlock routes and reduce transit costs.
- Dependencies: Transportation Planner, Atlas.
- Priority: Medium
- Version: v0.6
- Current Status: not implemented.

## Guide Generation

- Purpose: translate plans into human-readable guidance nodes.
- Dependencies: Journey, Navigator, Atlas.
- Priority: Medium
- Version: v0.7
- Current Status: not implemented.

## Completionist Path Support

- Purpose: support long-term cape goals like Completionist and Trimmed Completionist.
- Dependencies: Journey, Account Engine, Achievement Planner.
- Priority: Medium
- Version: v0.8
- Current Status: planned.

## Cross-Platform Web Experience

- Purpose: deliver a browser-based interface with responsive interaction.
- Dependencies: Frontend, API layer.
- Priority: High
- Version: v0.3
- Current Status: frontend skeleton exists.
