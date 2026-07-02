# AI Architecture Guidelines

## Purpose

This document explains how the AI should interpret and preserve Lodestone's architecture when making changes.

## Architectural Boundaries

- Atlas stores facts and domain data.
- Navigator handles routing, API contracts, and request orchestration.
- Advisor encapsulates business logic and decision-making.
- Forge imports game and player data.
- Journey defines player goals and progress.
- Forecast manages runtime configuration and environment.

## Design Principles

- Keep domain logic separate from transport and persistence.
- Use data-driven rules rather than hardcoded game mechanics.
- Support multiple account and journey types without assumptions.
- Prefer provider-based abstractions for external data.
- Preserve existing package boundaries unless a clear architecture issue exists.
