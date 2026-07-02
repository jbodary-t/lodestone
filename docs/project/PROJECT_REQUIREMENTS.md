# Lodestone Project Requirements

This document records engineering requirements for Lodestone as a long-lived progression optimization platform.

## Platform Requirements

- Support Windows, macOS (Intel), macOS (Apple Silicon), Linux, and modern web browsers.
- Avoid platform-specific implementation unless absolutely necessary.
- Design for future mobile support.
- Maintain cross-platform compatibility in core backend and provider code.

## Data and Architecture Requirements

- Atlas must store factual game data and remain the source of truth.
- Navigator must compute strategy and never be used as the authoritative facts database.
- Every domain concept must be data-driven.
- Every RuneScape concept in the system must be representable as an Activity.
- The application must be ironman-first in its first supported journey.
- No assumptions should be built around microtransactions or premium advantage.
- The system must support multiple data providers.
- The system should support Smart Capture implementations.
- The system should support RuneMetrics imports.
- The system should support Wiki Sync.
- The system should support future plugins and official APIs.

## Recommendation Requirements

- Every recommendation must explain WHY.
- Recommendations should eventually include:
  - confidence
  - opportunity cost
  - estimated time saved
  - future unlock value
  - travel savings
  - resource impact
- Recommendations should be expressed in terms of actionable progression steps.
- Recommendations should be traceable to account state and activity requirements.

## Account and Goal Requirements

- The system must support account creation and progress tracking.
- The first-run flow must capture game choice, goal, optimization level, and provider selection.
- Goals must be extensible from fresh ironman to completionist pathways.
- The system must support account state import from multiple provider sources.

## Provider Requirements

- Providers must be modular and replaceable.
- No system should rely on a single provider.
- Providers must map to canonical account and activity models.
- Providers should be validated and normalized before they reach the core engine.

## Quality and Maintainability Requirements

- Keep domain logic separate from persistence and transport.
- Prioritize explicit interfaces, typed contracts, and clean module boundaries.
- Avoid hardcoded game rules; define rules in data models and requirement definitions.
- Build the system so it can be extended without significant refactor.
- Maintain a stable API surface for backend consumers.
- Ensure every new system is accompanied by tests and documentation.

## Engineering Requirements

- Establish a dependency-driven build order before implementing new systems.
- Document system responsibilities, inputs, outputs, and blocked paths.
- Use provider adapters and integration layers for all external sources.
- Treat the backend as the authoritative engine and the frontend as a presentation layer.
- Keep recommendations explainable and auditable.
