# Journey Engine

The Journey Engine defines the player destination and captures the high-level goals needed for the recommendation system.

## Purpose

- Represent a player journey in a domain-first model.
- Persist journey definitions to support account-specific progression goals.
- Validate journey configuration before recommendation engines use it.
- Expose journey management via REST endpoints.
- Keep journey planning separate from route computation and recommendation logic.

## Core Concepts

- `Game`: RuneScape 3 (`RS3`) or Old School RuneScape (`OSRS`).
- `Account Type`: player account classification such as `standard`, `ironman`, `hardcore_ironman`, `ultimate_ironman`, and `group_ironman`.
- `Journey Type`: high-level objective categories including `trimmed_completionist`, `completionist`, `master_quest_cape`, `quest_cape`, `max_cape`, `skill_goal`, `boss_goal`, `collection_log`, and `custom`.
- `Optimization Mode`: planning style such as `explorer`, `pathfinder`, `navigator`, or `custom`.
- `Preferences`: soft guidance for the recommendation engine, e.g. `afk`, `minimize_dailies`, `minimize_cost`, `ironman_friendly`, `collection_log_focus`, `lore_focus`, `pvm_focus`, `skilling_focus`, `accessibility`.
- `Constraints`: explicit journey restrictions and policy guardrails.
- `Starting State`: current account snapshot and progress data.
- `Target State`: destination state describing the journey outcome.

## Validation

- Journey definitions require a valid `game`, `account_type`, `journey_type`, and `optimization_mode`.
- Preferences and constraints are normalized to unique ordered lists.
- `starting_state` and `target_state` must be JSON objects.
- Non-custom journey types must include a `target_state`.

## Persistence

Journeys are stored in the `journeys` database table with the following persisted fields:

- `account_id`
- `name`
- `description`
- `game`
- `account_type`
- `journey_type`
- `optimization_mode`
- `preferences`
- `constraints`
- `starting_state`
- `target_state`
- `status`
- `created_at`
- `updated_at`

## REST API

The backend exposes CRUD endpoints for journeys under `/api/journeys`:

- `POST /api/journeys/` — create a journey definition.
- `GET /api/journeys/` — list journeys, optionally filtered by `account_id`.
- `GET /api/journeys/{journey_id}` — read a journey.
- `PATCH /api/journeys/{journey_id}` — update a journey.
- `DELETE /api/journeys/{journey_id}` — delete a journey.

## Future direction

- Journey definitions will be consumed by the Navigator and recommendation engines.
- Recommendation logic remains separate; this engine only defines goal state and eligibility.
- Future work includes goal calibration, multi-step journey planning, and destination scoring.
