# Lodestone Engineering

## Welcome

This folder contains Lodestone's engineering foundation and planning documents. These pages describe the platform's vision, architecture, requirements, planned features, data providers, and first-run experience.

## What Lodestone Is

Lodestone is an open-source RuneScape progression optimization platform. It is a decision engine, not a wiki. Atlas stores facts. Navigator computes strategy. Everything in the system is modeled as an Activity.

## How to Navigate the Engineering Documents

- Vision → [PROJECT_MANIFEST.md](PROJECT_MANIFEST.md)
- Project Requirements → [PROJECT_REQUIREMENTS.md](PROJECT_REQUIREMENTS.md)
- Architecture → [SYSTEMS.md](SYSTEMS.md)
- Feature Planning → [FEATURE_MATRIX.md](FEATURE_MATRIX.md)
- Data Sources → [DATA_PROVIDERS.md](DATA_PROVIDERS.md)
- First Run Experience → [FIRST_RUN_EXPERIENCE.md](FIRST_RUN_EXPERIENCE.md)

---

## Vision

See the full platform vision in [PROJECT_MANIFEST.md](PROJECT_MANIFEST.md).

---

## Project Requirements

See the engineering requirements in [PROJECT_REQUIREMENTS.md](PROJECT_REQUIREMENTS.md).

---

## Architecture

See system descriptions, dependencies, and responsibilities in [SYSTEMS.md](SYSTEMS.md).

---

## Feature Planning

See planned user-facing capabilities and priorities in [FEATURE_MATRIX.md](FEATURE_MATRIX.md).

---

## Data Sources

See provider strategy and supported input channels in [DATA_PROVIDERS.md](DATA_PROVIDERS.md).

---

## First Run Experience

See the initial onboarding flow in [FIRST_RUN_EXPERIENCE.md](FIRST_RUN_EXPERIENCE.md).

---

## Current Development Stage

- Current stage: Engineering foundation and requirement engine alignment.
- Current milestone: Establish the Lodestone engineering foundation.
- Current GitHub issue: Issue #3 — Establish the Engineering Manifest.
- Next planned issue: Complete the Requirement Evaluator and add unit tests.

---

## Development Philosophy

- Atlas stores facts.
- Navigator computes strategy.
- Everything is an Activity.
- Everything is data-driven.
- Ironman-first.
- Cross-platform.
- Support RS3 and OSRS.
- No MTX assumptions.

---

## How to Add a New System

1. Define the system's purpose and responsibilities.
2. Document its dependencies, inputs, outputs, consumers, and blocked systems.
3. Add the system to [SYSTEMS.md](SYSTEMS.md) with a clear description.
4. Add any required feature planning entries to [FEATURE_MATRIX.md](FEATURE_MATRIX.md).
5. Update [PROJECT_MANIFEST.md](PROJECT_MANIFEST.md) if the system changes the overall architecture.

---

## How to Add a New Feature

1. Confirm the feature aligns with Lodestone's vision and engineering principles.
2. Describe the feature's purpose, dependencies, priority, version target, and status.
3. Add the feature to [FEATURE_MATRIX.md](FEATURE_MATRIX.md).
4. If the feature depends on new requirements, update [PROJECT_REQUIREMENTS.md](PROJECT_REQUIREMENTS.md).
5. If the feature requires new data sources, update [DATA_PROVIDERS.md](DATA_PROVIDERS.md).

---

## How to Add a New Data Provider

1. Define the provider type and supported inputs.
2. Ensure the provider maps to canonical Atlas models.
3. Document it in [DATA_PROVIDERS.md](DATA_PROVIDERS.md).
4. If needed, update [PROJECT_REQUIREMENTS.md](PROJECT_REQUIREMENTS.md) with provider expectations.
5. Keep the provider implementation decoupled from Navigator strategy logic.

---

## How to Contribute

- Start by reading the engineering documents in this folder.
- Open issues for new systems, features, or provider support.
- Keep changes focused on clear system boundaries and documented requirements.
- Add tests and documentation for every new capability.
- Preserve the separation between factual data (Atlas) and strategy/recommendation logic (Navigator).
