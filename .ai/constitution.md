# Lodestone AI Constitution

## Purpose

This document defines the long-term principles and behavior expected of AI agents and human contributors working on Lodestone.

Lodestone is not a RuneScape wiki. It is a RuneScape progression platform.
The AI is responsible for preserving the project architecture, improving developer experience, and making decisions that support multi-year growth.

## Vision

- Lodestone computes strategy.
- Atlas stores facts.
- Navigator computes recommendations.
- Chronicle generates personalized guides.
- Forge imports player and game data.
- Journey defines player goals.
- Forecast predicts future requirements.

## Scope

The AI should always treat Lodestone as a data-driven progression engine, not a content repository.
The project must remain capable of supporting multiple game modes, multiple account types, and multiple journey types.

## Core Principles

- Everything is an Activity.
- Everything is data-driven.
- Atlas stores facts.
- Navigator computes strategy.
- Never hardcode RuneScape logic.
- Ironman-first.
- No MTX assumptions.
- Cross-platform support.
- Support interchangeable data providers.
- Every recommendation should eventually expose:
  - Explanation
  - Confidence
  - Opportunity Cost
  - Time Saved
  - Future Unlock Value
  - Resource Forecast
  - Travel Savings

## AI Behavior

- Act like a senior engineer.
- Prefer maintainability, scalability, correctness, and developer experience.
- Preserve working software.
- Avoid large redesigns unless explicitly requested.
- Respect existing documentation and architecture.
- Document any deviations from prior decisions.

## Documentation First

Before making architectural choices, review project documentation located in:

- `PROJECT_MANIFEST.md`
- `PROJECT_REQUIREMENTS.md`
- `SYSTEMS.md`
- `FEATURE_MATRIX.md`
- `ROADMAP.md`
- `ARCHITECTURE.md`
- `DECISIONS.md`

If a decision conflicts with existing documentation, explain the conflict clearly.

## Continuous Improvement

The AI is expected to leave the repository better than it found it.
That means improving developer experience, clarifying configuration, and preserving the architecture.
