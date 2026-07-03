# Lodestone Development Roadmap

> **Vision:** Build an intelligent RuneScape progression platform that helps players determine the optimal next action based on their account, goals, and preferences.

---

## Development Rules

These rules define how Lodestone is developed and are considered part of the project's engineering standards.

### 1. One Active Epic

Only one Epic may be actively developed at a time.

A new Epic may not begin until the previous Epic has been completed, reviewed, and frozen (if applicable).

---

### 2. Epic Completion Requirements

An Epic is considered complete only when all of the following are true:

- All planned features for the Epic are implemented.
- All tests pass.
- Backend starts successfully.
- Frontend builds successfully.
- Documentation is fully updated.
- Architecture review has been completed.
- Technical debt has been documented.
- Engineering summary has been produced.
- Changes have been committed.
- A Git tag has been created for the completed Epic.

---

### 3. Engine Development Process

All core Lodestone engines must follow the same development lifecycle.

1. Architecture Design
2. Specification
3. Domain Model
4. Public API Design
5. Infrastructure Implementation
6. Feature Implementation
7. Testing
8. Documentation
9. Architecture Review
10. Freeze

Implementation begins only after the specification has been approved.

---

### 4. Architecture Authority

Core architecture decisions are made by the project owner.

AI assistants (Continue, ChatGPT, or future agents) may:

- Implement approved specifications.
- Improve code quality.
- Refactor safely.
- Improve documentation.
- Improve performance.
- Fix bugs.

AI assistants may NOT:

- Invent new engine architecture.
- Change public APIs.
- Change engine responsibilities.
- Merge responsibilities between engines.
- Introduce breaking architectural changes.

These require explicit approval.

---

### 5. Engine Responsibilities

Every engine must have a single responsibility.

Current platform architecture:

- Atlas → RuneScape knowledge graph
- Journey Engine → Progression planning
- Navigator → Decision making
- Guide Engine → Presentation logic
- Guide Mode → User Interface
- Chronicle → Player history and analytics

Responsibilities should never overlap.

---

### 6. Documentation First

Every major subsystem must include:

- Specification
- Public API documentation
- Architecture documentation
- Engineering summary
- Readiness report

Documentation is considered part of the implementation.

---

### 7. Definition of Freeze

When an engine is frozen:

Allowed:

- Bug fixes
- Performance improvements
- Additional data/content
- Internal refactoring that does not change public behavior

Requires an Architecture Decision Record (ADR):

- Public API changes
- Domain model changes
- Responsibility changes
- Breaking changes
- Folder structure changes

---

### 8. Quality Standards

All new code should prioritize:

- Maintainability
- Readability
- Extensibility
- Modularity
- Testability
- Performance
- Clear separation of responsibilities

Premature optimization should be avoided unless profiling indicates it is necessary.

---

### 9. AI Workflow

Continue is responsible for implementation.

ChatGPT is responsible for:

- Architecture
- System design
- Specifications
- Engineering reviews
- Long-term planning
- Code review guidance

The project owner retains final authority over all architectural decisions.

---

### 10. Project Philosophy

Lodestone is an engine-driven platform.

Features are built on top of engines—not the other way around.

Every architectural decision should improve the platform's ability to evolve over many years without requiring large-scale rewrites.

---

# Platform Status

## ✅ Epic 0 – Foundation
**Status:** Complete

### Goals
- [x] Backend foundation
- [x] Frontend foundation
- [x] GitHub repository
- [x] Local AI development workflow
- [x] Continue + Ollama integration
- [x] AI documentation framework
- [x] Development standards
- [x] Health monitoring
- [x] Build pipeline

---

## ✅ Epic 1 – Atlas Engine
**Status:** Complete (Frozen)

### Purpose
Atlas is Lodestone's knowledge engine.

Atlas knows RuneScape.

Atlas does NOT make decisions.

### Completed

#### Core Architecture
- [x] AtlasNode
- [x] Relationship model
- [x] Entity hierarchy
- [x] Repository layer
- [x] Provider layer
- [x] Query engine
- [x] Graph traversal
- [x] Dependency graph
- [x] Validation
- [x] Serialization

#### Intelligence
- [x] Unlock graph
- [x] Missing requirements
- [x] Shortest path
- [x] Circular dependency detection
- [x] Dependency analysis
- [x] Graph indexing

#### Engineering
- [x] Documentation
- [x] Public API
- [x] Unit tests
- [x] Architecture review
- [x] Readiness report

### Freeze Policy

Allowed:
- Bug fixes
- Performance improvements
- Additional RuneScape content
- New providers

Requires ADR:
- Public API changes
- Entity model changes
- Relationship model changes

---

# Epic 2 – Journey Engine
**Status:** Next

### Purpose

Consumes Atlas.

Builds progression plans.

Tracks goals.

Generates dependency trees.

Creates optimized journeys.

### Planned

- [ ] Journey model
- [ ] Goal system
- [ ] Dependency planner
- [ ] Progress planner
- [ ] Milestone system
- [ ] Optimization framework
- [ ] Journey persistence
- [ ] Journey API
- [ ] Unit tests
- [ ] Documentation

---

# Epic 3 – Navigator
**Status:** Planned

### Purpose

Consumes Atlas and Journey Engine.

Calculates the player's optimal next action.

### Planned

- [ ] Recommendation engine
- [ ] Priority scoring
- [ ] Requirement evaluation
- [ ] Opportunity analysis
- [ ] Route selection
- [ ] Recommendation API

---

# Epic 4 – Guide Engine
**Status:** Planned

### Purpose

Consumes Navigator.

Transforms recommendations into interactive guides.

### Planned

- [ ] Guide sessions
- [ ] Widget registry
- [ ] Step renderer
- [ ] Progress renderer
- [ ] Layout manager
- [ ] Guide API

---

# Epic 5 – Guide Mode UI
**Status:** Planned

### Purpose

Compact in-game interface.

### Planned

- [ ] Docking
- [ ] Floating
- [ ] Widget layouts
- [ ] Resize
- [ ] Opacity
- [ ] Multiple layouts
- [ ] Theme support
- [ ] Accessibility

---

# Epic 6 – Chronicle
**Status:** Planned

### Purpose

Player history and analytics.

### Planned

- [ ] Session history
- [ ] Timeline
- [ ] Milestones
- [ ] Analytics
- [ ] Statistics
- [ ] Reports

---

# Epic 7 – Player Simulation
**Status:** Planned

### Purpose

Provide a simulated RuneScape account for development and testing.

### Planned

- [ ] Simulated player profile
- [ ] Skills
- [ ] Quests
- [ ] Inventory
- [ ] Equipment
- [ ] Teleports
- [ ] Unlock tracking
- [ ] State persistence

---

# Epic 8 – Live Integrations
**Status:** Planned

### Planned

- [ ] RuneMetrics
- [ ] OCR
- [ ] Screenshot recognition
- [ ] Manual synchronization
- [ ] Plugin framework

---

# Epic 9 – Polish & Release

### Planned

- [ ] Performance
- [ ] Accessibility
- [ ] Error handling
- [ ] Documentation
- [ ] Packaging
- [ ] Installer
- [ ] Release Candidate

---

## Future Epics (Not Yet Scheduled)

- Clue Engine
- OCR Engine
- Overlay Engine
- Boss Engine
- Collection Log Engine
- Achievement Assistant
- Mobile Companion
- Cloud Sync
- Plugin System

These Epics are intentionally deferred until the core platform
(Atlas, Journey Engine, Navigator, and Guide Engine) is complete and stable.