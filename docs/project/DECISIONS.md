# Lodestone Architecture Decision Records (ADRs)

This file records major architectural decisions for Lodestone. Each ADR includes the decision context, rationale, and consequences.

## ADR-001: Everything is an Activity

- Status: Accepted
- Date: 2026-07-02

### Context
Lodestone must model RuneScape progression in a unified, extensible way. Multiple domain concepts exist: quests, bosses, achievements, diaries, minigames, transportation, skill training, and collection logs.

### Decision
Represent every RuneScape progression concept as an Activity.

### Consequences
- The core domain model is simplified and extensible.
- All systems can operate against a single canonical object type.
- Future activity subtypes can be added without changing strategy engine contracts.

### Alternatives Considered
- Maintain separate domain types for each progression concept.
- Use hybrid models where only some concepts are activities.

## ADR-002: Atlas stores facts. Navigator computes strategy.

- Status: Accepted
- Date: 2026-07-02

### Context
The platform needs a clear separation between factual data and strategic recommendation logic.

### Decision
Atlas is the authoritative factual data layer. Navigator is the strategy and recommendation engine.

### Consequences
- Data ingestion and provider integration are isolated from recommendation logic.
- Strategy engines can remain provider-agnostic.
- The platform avoids mixing wiki-style facts with progression decisions.

### Alternatives Considered
- Use a single data layer for both facts and recommendations.
- Embed strategy rules directly in provider adapters.

## ADR-003: Support multiple interchangeable data providers.

- Status: Accepted
- Date: 2026-07-02

### Context
Lodestone must ingest account and game data from a variety of sources without relying on a single provider.

### Decision
Design provider adapters so that data sources are interchangeable and mapped into canonical Atlas models.

### Consequences
- The platform can support Wiki Sync, RuneMetrics, manual entry, CSV import, Smart Capture, plugins, and future APIs.
- No system depends on one provider implementation.
- Provider-specific logic stays in adapter layers.

### Alternatives Considered
- Build around one primary provider with limited secondary sources.
- Hardcode provider formats into the core engine.

## ADR-004: Ironman-first architecture.

- Status: Accepted
- Date: 2026-07-02

### Context
The first supported journey is Fresh RS3 Ironman to Trimmed Completionist Cape.

### Decision
Prioritize Ironman account modeling, progression constraints, and provider assumptions in the initial architecture.

### Consequences
- Early architecture supports restrictions and optimization patterns unique to Ironman play.
- Future modes like standard and hardcore can be added with explicit account modes.
- Strategy engines can incorporate Ironman-specific constraints from the start.

### Alternatives Considered
- Build a generic RuneScape planner first.
- Start with standard account assumptions and retrofit Ironman behavior later.

## ADR-005: Cross-platform support.

- Status: Accepted
- Date: 2026-07-02

### Context
Lodestone must serve users on Windows, macOS, Linux, and the web.

### Decision
Design all core systems and tooling to avoid platform-specific dependencies and favor cross-platform compatibility.

### Consequences
- Development tooling must be portable.
- Native code or OS-specific optimizations are deferred unless absolutely required.
- The platform remains accessible to a broad developer and user base.

### Alternatives Considered
- Prioritize a single platform and expand later.
- Accept platform-specific implementations for early speed.

## ADR-006: Separate Facts from Strategy throughout the application.

- Status: Accepted
- Date: 2026-07-02

### Context
Mixing facts and strategy makes the system brittle and harder to extend.

### Decision
Maintain a strict separation between factual data models and strategy/recommendation logic across all systems.

### Consequences
- Facts remain reusable across engines and providers.
- Strategy engines can evolve independently from data ingestion.
- The platform better supports provider replacement and long-term maintenance.

### Alternatives Considered
- Use shared data structures for both facts and strategy.
- Allow strategic annotations in factual models.

## ADR-007: Use dependency-driven development. Systems are built before features.

- Status: Accepted
- Date: 2026-07-02

### Context
Lodestone is a complex platform with many systems that depend on one another.

### Decision
Build systems in a dependency-driven order and avoid implementing features before their required systems exist.

### Consequences
- Implementation order is predictable and maintainable.
- Features are built on stable foundations.
- Technical debt from premature feature work is reduced.

### Alternatives Considered
- Build features opportunistically as they become visible.
- Prioritize visible frontend features before backend systems.

## ADR-008: The RuneScape Wiki is the primary source of factual game data. Lodestone builds optimization on top of those facts.

- Status: Accepted
- Date: 2026-07-02

### Context
Lodestone needs a reliable source for canonical game facts.

### Decision
Treat official or community-maintained RuneScape Wiki data as the primary factual source and build optimization layers on top.

### Consequences
- Facts are sourced from well-established game data.
- The platform can focus on optimization rather than fact discovery.
- Wiki Sync becomes the foundational provider for Atlas.

### Alternatives Considered
- Use game APIs as the primary factual feed.
- Build facts from player-submitted data first.

## ADR-009: Smart Capture is a first-class data provider.

- Status: Accepted
- Date: 2026-07-02

### Context
Account state capture is critical for user adoption and data completeness.

### Decision
Design Smart Capture as a first-class provider for screenshots, OCR, and capture pipelines.

### Consequences
- Users can import account data from live screen sources.
- The platform supports bank, equipment, boss log, achievements, and collection data capture.
- OCR and capture integration become central capabilities rather than optional addons.

### Alternatives Considered
- Treat Smart Capture as a lower-priority integration.
- Rely only on manual entry and API imports.

## ADR-010: Every recommendation must include an explanation so users understand why it was chosen.

- Status: Accepted
- Date: 2026-07-02

### Context
Recommendations are only useful if users trust and understand them.

### Decision
Every recommendation must include a clear explanation of why it was chosen.

### Consequences
- The platform supports explainability and user trust.
- Recommendation outputs must include rationale and evidence.
- Recommendation engines must expose reasoning data.

### Alternatives Considered
- Generate recommendations without explicit explanations.
- Provide only numerical scores and rankings.
