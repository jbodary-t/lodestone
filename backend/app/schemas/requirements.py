from __future__ import annotations

import uuid
from enum import StrEnum
from typing import Annotated, Union
from pydantic import BaseModel, Field


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


class RequirementBase(BaseModel):
    type: RequirementType
    description: str | None = None

    class Config:
        orm_mode = True


class SkillRequirement(RequirementBase):
    type: RequirementType = Field(default=RequirementType.SKILL, const=True)
    skill: str
    level: int


class QuestRequirement(RequirementBase):
    type: RequirementType = Field(default=RequirementType.QUEST, const=True)
    quest_id: uuid.UUID


class QuestPointsRequirement(RequirementBase):
    type: RequirementType = Field(default=RequirementType.QUEST_POINTS, const=True)
    minimum_points: int


class AchievementRequirement(RequirementBase):
    type: RequirementType = Field(default=RequirementType.ACHIEVEMENT, const=True)
    achievement_id: uuid.UUID


class DiaryRequirement(RequirementBase):
    type: RequirementType = Field(default=RequirementType.DIARY, const=True)
    diary_id: uuid.UUID


class ItemRequirement(RequirementBase):
    type: RequirementType = Field(default=RequirementType.ITEM, const=True)
    item_id: uuid.UUID
    quantity: int


class AreaRequirement(RequirementBase):
    type: RequirementType = Field(default=RequirementType.AREA_UNLOCK, const=True)
    area_id: uuid.UUID


class TransportUnlockRequirement(RequirementBase):
    type: RequirementType = Field(default=RequirementType.TRANSPORT_UNLOCK, const=True)
    transport_id: uuid.UUID


class BossKillCountRequirement(RequirementBase):
    type: RequirementType = Field(default=RequirementType.BOSS_KILL_COUNT, const=True)
    boss_id: uuid.UUID
    kill_count: int


class CombatLevelRequirement(RequirementBase):
    type: RequirementType = Field(default=RequirementType.COMBAT_LEVEL, const=True)
    minimum_level: int


class NecromancyTalentRequirement(RequirementBase):
    type: RequirementType = Field(default=RequirementType.NECROMANCY_TALENT, const=True)
    required_talent: int


class CollectionLogRequirement(RequirementBase):
    type: RequirementType = Field(default=RequirementType.COLLECTION_LOG, const=True)
    entry_id: uuid.UUID


class ArchaeologyMysteryRequirement(RequirementBase):
    type: RequirementType = Field(default=RequirementType.ARCHAEOLOGY_MYSTERY, const=True)
    mystery_id: uuid.UUID


class ResearchRequirement(RequirementBase):
    type: RequirementType = Field(default=RequirementType.RESEARCH, const=True)
    research_id: uuid.UUID


class PlayerOwnedFarmRequirement(RequirementBase):
    type: RequirementType = Field(default=RequirementType.PLAYER_OWNED_FARM, const=True)


class PortsProgressRequirement(RequirementBase):
    type: RequirementType = Field(default=RequirementType.PORTS_PROGRESS, const=True)
    region_id: uuid.UUID


RequirementSchema = Annotated[
    Union[
        SkillRequirement,
        QuestRequirement,
        QuestPointsRequirement,
        AchievementRequirement,
        DiaryRequirement,
        ItemRequirement,
        AreaRequirement,
        TransportUnlockRequirement,
        BossKillCountRequirement,
        CombatLevelRequirement,
        NecromancyTalentRequirement,
        CollectionLogRequirement,
        ArchaeologyMysteryRequirement,
        ResearchRequirement,
        PlayerOwnedFarmRequirement,
        PortsProgressRequirement,
    ],
    Field(discriminator="type"),
]
