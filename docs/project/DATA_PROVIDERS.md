# Lodestone Data Providers

Lodestone is designed to support interchangeable source providers. The system must never depend on only one provider.

## Wiki Sync

- Description: import factual game data from RuneScape Wiki sources and canonical game databases.
- Inputs: activity metadata, item data, quest information, rewards, unlock definitions.
- Status: planned.
- Considerations:
  - must be replaceable and versioned
  - should support manual or scheduled sync
  - must avoid embedding wiki logic in the recommendation engine

## RuneMetrics

- Description: import player account progress from RuneMetrics reports and exportable data.
- Inputs: skills, quests, achievements, equipment, resource counts.
- Status: planned.
- Considerations:
  - mapped to canonical account progress
  - must preserve privacy and export consent
  - should integrate with account setup and smart capture

## Manual Entry

- Description: allow users to enter account state manually through a form or guided setup.
- Inputs: skill levels, quest completion, diary status, item counts, unlocks.
- Status: foundational requirement.
- Considerations:
  - must support partial data and progressive entry
  - should be the fallback for every provider path

## CSV Import

- Description: ingest structured account and activity data from CSV exports.
- Inputs: skill tables, quest tables, item lists, account inventories.
- Status: planned.
- Considerations:
  - should support multiple CSV formats via mapping templates
  - must include validation and user feedback on mismatched fields

## Smart Capture (OCR)

- Description: convert screenshots and screen captures into account progress data.
- Inputs: skill panels, quest lists, bank screens, equipment, boss logs, achievement panels, collection log screens.
- Status: planned.
- Considerations:
  - should support paste, drag-and-drop, and region capture
  - must feed into the Account Engine
  - must be extensible for new capture patterns and games

## Future Official APIs

- Description: integrate official RuneScape APIs when available.
- Inputs: authenticated account data, progression state, official game metadata.
- Status: planned.
- Considerations:
  - must remain decoupled from provider-specific logic
  - should use adapter patterns to maintain a stable core

## Future Plugins

- Description: plugin architecture for new provider integrations and external services.
- Inputs: any supported data payloads from third-party sources.
- Status: planned.
- Considerations:
  - should expose a stable provider interface
  - must support safe extension without modifying core engine behavior

## Provider Principles

- Providers must be interchangeable.
- Providers must map to canonical Atlas models.
- Providers must not alter recommendation strategy directly.
- Providers should offer traceable import provenance.
