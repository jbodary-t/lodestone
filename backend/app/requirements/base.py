from __future__ import annotations

from enum import StrEnum
from typing import Protocol
import uuid
from pydantic import BaseModel


class RequirementType(StrEnum):
    SKILL = "skill"
    QUEST = "quest"
    QUEST_POINTS = "quest_points"
    ACHIEVEMENT = "achievement"
    DIARY = "diary"
    ITEM = "item"
    AREA_UNLOCK = "area_unlock"
    TRANSPORT_UNLOCK = "transport_unlock"
    BOSS_KILL_COUNT = "boss_kill_count"
    COMBAT_LEVEL = "combat_level"
    NECROMANCY_TALENT = "necromancy_talent"
    COLLECTION_LOG = "collection_log"
    ARCHAEOLOGY_MYSTERY = "archaeology_mystery"
    RESEARCH = "research"
    PLAYER_OWNED_FARM = "player_owned_farm"
    PORTS_PROGRESS = "ports_progress"


class Requirement(BaseModel):
    type: RequirementType

    def is_satisfied(self, account: "AccountProgress") -> bool:
        raise NotImplementedError


class AccountProgress(Protocol):
    def has_skill(self, skill: str, level: int) -> bool:
        ...

    def has_completed_quest(self, quest_id: uuid.UUID) -> bool:
        ...

    def quest_points(self) -> int:
        ...

    def has_achievement(self, achievement_id: uuid.UUID) -> bool:
        ...

    def has_diary(self, diary_id: uuid.UUID) -> bool:
        ...

    def has_item(self, item_id: uuid.UUID, quantity: int) -> bool:
        ...

    def has_area_unlock(self, area_id: uuid.UUID) -> bool:
        ...

    def has_transport_unlock(self, transport_id: uuid.UUID) -> bool:
        ...

    def boss_kill_count(self, boss_id: uuid.UUID) -> int:
        ...

    def combat_level(self) -> int:
        ...

    def necromancy_talent(self) -> int:
        ...

    def has_collection_log(self, entry_id: uuid.UUID) -> bool:
        ...

    def archaeology_mystery(self, mystery_id: uuid.UUID) -> bool:
        ...

    def has_research(self, research_id: uuid.UUID) -> bool:
        ...

    def has_player_owned_farm(self) -> bool:
        ...

    def ports_progress(self, region_id: uuid.UUID) -> bool:
        ...
