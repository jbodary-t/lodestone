# Lodestone Systems

This document describes Lodestone's backend systems, their responsibilities, and their dependencies.

## Activity Engine

- Purpose: represent everything in RuneScape as an Activity and maintain canonical activity definitions.
- Dependencies: Atlas, Account Engine, Requirement Engine.
- Inputs: activity metadata, tags, relationships, account state.
- Outputs: activity objects, activity graphs, activity metadata for planners.
- Consumers: Navigator, Journey, Reward Engine, API layer.
- Blocked Systems: Navigator, Journey.
- Future Extensions: activity subtypes for quests, bosses, minigames, transportation, collection logs, diaries, and skill training.

## Requirement Engine

- Purpose: evaluate activity prerequisites against account progress.
- Dependencies: Atlas, Account Engine, Activity Engine.
- Inputs: activity requirements, account progress, inventory, unlocks.
- Outputs: satisfied/unsatisfied requirement states, missing requirements, requirement rationale.
- Consumers: Navigator, Journey, Recommendation Engine.
- Blocked Systems: Navigator, Journey, Guide Generator.
- Future Extensions: composite requirements, grouped requirements, optional requirement tiers, conflict detection.

## Reward Engine

- Purpose: quantify the outcomes and value of completing an activity.
- Dependencies: Atlas, Activity Engine.
- Inputs: activity outcomes, resource inputs/outputs, unlock values, reward tags.
- Outputs: reward impact, resource estimates, unlock value, future benefit signals.
- Consumers: Navigator, Journey, Guide Generator.
- Blocked Systems: Navigator.
- Future Extensions: economic modeling, opportunity cost analysis, resource efficiency scoring.

## Account Engine

- Purpose: capture and maintain player account state, progression, and imported data.
- Dependencies: Atlas, Data Providers.
- Inputs: account metadata, skills, inventory, quests, achievements, diary progress, collection log progress.
- Outputs: canonical account progress, account health state, account capability profile.
- Consumers: Requirement Engine, Navigator, Journey, Recommendation Engine.
- Blocked Systems: Requirement Engine, Navigator.
- Future Extensions: multi-account support, account comparison, account health diagnostics.

## Atlas

- Purpose: store factual game data and unify provider inputs into a canonical model.
- Dependencies: Data Providers.
- Inputs: provider import data, wiki sync data, official API data.
- Outputs: canonical activity facts, item metadata, quest metadata, unlock definitions.
- Consumers: Account Engine, Activity Engine, Requirement Engine, Reward Engine, Navigator.
- Blocked Systems: Account Engine, Requirement Engine.
- Future Extensions: provider reconciliation, versioned fact stores, offline fact cache.

## Navigator

- Purpose: calculate prioritized progression recommendations.
- Dependencies: Requirement Engine, Reward Engine, Account Engine, Atlas.
- Inputs: account state, activity definitions, requirement satisfaction, reward estimates, goal selection.
- Outputs: ranked recommendations with explanation, confidence, and risk signals.
- Consumers: Journey, Guide Generator, API layer.
- Blocked Systems: Journey, Guide Generator.
- Future Extensions: optimization levels, strategy modes, risk-aware recommendations.

## Forecast

- Purpose: manage runtime configuration, environment settings, and external dependency configuration.
- Dependencies: platform runtime, environment variables.
- Inputs: settings, environment variables, runtime flags.
- Outputs: configured application context, database connections, provider endpoints.
- Consumers: all backend systems.
- Blocked Systems: none.
- Future Extensions: feature flags, multi-instance configuration.

## Journey

- Purpose: sequence activities into a goal-driven plan.
- Dependencies: Navigator, Account Engine, Activity Engine.
- Inputs: selected goal, current progress, recommendations, requirement state.
- Outputs: itinerary, milestones, progression checkpoints.
- Consumers: Guide Generator, API layer.
- Blocked Systems: Guide Generator.
- Future Extensions: branching journeys, goal templates, scenario planning.

## Guide Generator

- Purpose: create explainable, human-readable plans from journey and recommendation data.
- Dependencies: Journey, Atlas, Navigator.
- Inputs: planned activities, rationale, account context.
- Outputs: structured guides, task narratives, recommended workflows.
- Consumers: frontend, export interfaces.
- Blocked Systems: none.
- Future Extensions: natural-language generation, adaptive guides, multi-format exports.

## Bank Advisor

- Purpose: analyze bank holdings and recommend inventory or acquisition plans.
- Dependencies: Account Engine, Atlas, Reward Engine.
- Inputs: bank contents, activity requirements, resource needs.
- Outputs: bank recommendations, item acquisition strategies.
- Consumers: Navigator, Journey.
- Blocked Systems: none.
- Future Extensions: bank optimization, loot forecasting, economy-aware decisions.

## PvM Planner

- Purpose: plan boss and combat progression based on account capability.
- Dependencies: Account Engine, Activity Engine, Reward Engine.
- Inputs: account combat profile, boss requirements, reward value.
- Outputs: boss progression plans, unlock queues.
- Consumers: Navigator, Guide Generator.
- Blocked Systems: none.
- Future Extensions: raid planning, group composition, encounter readiness.

## Achievement Planner

- Purpose: sequence achievement goals and completion objectives.
- Dependencies: Account Engine, Activity Engine, Requirement Engine.
- Inputs: achievement progress, activity outcomes, account unlocks.
- Outputs: achievement funnels, completion milestones.
- Consumers: Navigator, Journey.
- Blocked Systems: none.
- Future Extensions: completionist plan modeling, trimmed cape pathways.

## XP Planner

- Purpose: model skill training progression and XP targets.
- Dependencies: Account Engine, Activity Engine.
- Inputs: skills, activity XP rewards, training methods.
- Outputs: XP plans, level estimates, skill priority recommendations.
- Consumers: Navigator, Journey.
- Blocked Systems: none.
- Future Extensions: training efficiency scoring, burnout avoidance.

## Resource Planner

- Purpose: manage resource consumption, item requirements, and supply chains.
- Dependencies: Account Engine, Atlas, Reward Engine.
- Inputs: item requirements, activity resource use, bank state.
- Outputs: resource plans, supply notifications, procurement recommendations.
- Consumers: Navigator, Journey, Bank Advisor.
- Blocked Systems: none.
- Future Extensions: trade modeling, farming plans, resource staging.

## Transportation Planner

- Purpose: recommend travel and unlock routes to minimize transit costs.
- Dependencies: Atlas, Account Engine, Activity Engine.
- Inputs: travel unlocks, teleport availability, distance metrics.
- Outputs: transportation plans, unlock sequencing advice.
- Consumers: Navigator, Journey.
- Blocked Systems: none.
- Future Extensions: route optimization, cost savings estimates.
