from __future__ import annotations

import uuid
from enum import StrEnum
from sqlalchemy import (
    Boolean,
    Column,
    Enum,
    ForeignKey,
    Integer,
    String,
    Text,
)
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


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


class ActivityRequirement(Base):
    __tablename__ = "activity_requirements"

    id: Mapped[int] = mapped_column(primary_key=True)
    activity_id: Mapped[uuid.UUID] = mapped_column(
        PG_UUID(as_uuid=True), ForeignKey("activities.id"), nullable=False
    )
    type: Mapped[RequirementType] = mapped_column(
        Enum(RequirementType, name="requirement_type", native_enum=False), nullable=False
    )
    description: Mapped[str | None] = mapped_column(String(length=400), nullable=True)

    activity = relationship("Activity", back_populates="requirements")

    __mapper_args__ = {
        "polymorphic_on": type,
        "polymorphic_identity": "activity_requirement",
        "with_polymorphic": "*",
    }

    def is_satisfied(self, account: "AccountProgress") -> bool:
        raise NotImplementedError

    def missing_items(self, account: "AccountProgress") -> list[uuid.UUID]:
        return []

    def missing_skills(self, account: "AccountProgress") -> list[str]:
        return []

    def missing_quests(self, account: "AccountProgress") -> list[uuid.UUID]:
        return []


class SkillRequirement(ActivityRequirement):
    __tablename__ = "skill_requirements"

    id: Mapped[int] = mapped_column(ForeignKey("activity_requirements.id"), primary_key=True)
    skill: Mapped[str] = mapped_column(String(length=100), nullable=False)
    level: Mapped[int] = mapped_column(Integer, nullable=False)

    __mapper_args__ = {
        "polymorphic_identity": RequirementType.SKILL,
    }

    def is_satisfied(self, account: "AccountProgress") -> bool:
        return account.has_skill(self.skill, self.level)

    def missing_skills(self, account: "AccountProgress") -> list[str]:
        return [] if self.is_satisfied(account) else [self.skill]


class QuestRequirement(ActivityRequirement):
    __tablename__ = "quest_requirements"

    id: Mapped[int] = mapped_column(ForeignKey("activity_requirements.id"), primary_key=True)
    quest_id: Mapped[uuid.UUID] = mapped_column(PG_UUID(as_uuid=True), nullable=False)

    __mapper_args__ = {
        "polymorphic_identity": RequirementType.QUEST,
    }

    def is_satisfied(self, account: "AccountProgress") -> bool:
        return account.has_completed_quest(self.quest_id)

    def missing_quests(self, account: "AccountProgress") -> list[uuid.UUID]:
        return [] if self.is_satisfied(account) else [self.quest_id]


class QuestPointsRequirement(ActivityRequirement):
    __tablename__ = "quest_points_requirements"

    id: Mapped[int] = mapped_column(ForeignKey("activity_requirements.id"), primary_key=True)
    minimum_points: Mapped[int] = mapped_column(Integer, nullable=False)

    __mapper_args__ = {
        "polymorphic_identity": RequirementType.QUEST_POINTS,
    }

    def is_satisfied(self, account: "AccountProgress") -> bool:
        return account.quest_points() >= self.minimum_points


class AchievementRequirement(ActivityRequirement):
    __tablename__ = "achievement_requirements"

    id: Mapped[int] = mapped_column(ForeignKey("activity_requirements.id"), primary_key=True)
    achievement_id: Mapped[uuid.UUID] = mapped_column(PG_UUID(as_uuid=True), nullable=False)

    __mapper_args__ = {
        "polymorphic_identity": RequirementType.ACHIEVEMENT,
    }

    def is_satisfied(self, account: "AccountProgress") -> bool:
        return account.has_achievement(self.achievement_id)


class DiaryRequirement(ActivityRequirement):
    __tablename__ = "diary_requirements"

    id: Mapped[int] = mapped_column(ForeignKey("activity_requirements.id"), primary_key=True)
    diary_id: Mapped[uuid.UUID] = mapped_column(PG_UUID(as_uuid=True), nullable=False)

    __mapper_args__ = {
        "polymorphic_identity": RequirementType.DIARY,
    }

    def is_satisfied(self, account: "AccountProgress") -> bool:
        return account.has_diary(self.diary_id)


class ItemRequirement(ActivityRequirement):
    __tablename__ = "item_requirements"

    id: Mapped[int] = mapped_column(ForeignKey("activity_requirements.id"), primary_key=True)
    item_id: Mapped[uuid.UUID] = mapped_column(PG_UUID(as_uuid=True), nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)

    __mapper_args__ = {
        "polymorphic_identity": RequirementType.ITEM,
    }

    def is_satisfied(self, account: "AccountProgress") -> bool:
        return account.has_item(self.item_id, self.quantity)

    def missing_items(self, account: "AccountProgress") -> list[uuid.UUID]:
        return [] if self.is_satisfied(account) else [self.item_id]


class AreaRequirement(ActivityRequirement):
    __tablename__ = "area_requirements"

    id: Mapped[int] = mapped_column(ForeignKey("activity_requirements.id"), primary_key=True)
    area_id: Mapped[uuid.UUID] = mapped_column(PG_UUID(as_uuid=True), nullable=False)

    __mapper_args__ = {
        "polymorphic_identity": RequirementType.AREA_UNLOCK,
    }

    def is_satisfied(self, account: "AccountProgress") -> bool:
        return account.has_area_unlock(self.area_id)


class TransportUnlockRequirement(ActivityRequirement):
    __tablename__ = "transport_unlock_requirements"

    id: Mapped[int] = mapped_column(ForeignKey("activity_requirements.id"), primary_key=True)
    transport_id: Mapped[uuid.UUID] = mapped_column(PG_UUID(as_uuid=True), nullable=False)

    __mapper_args__ = {
        "polymorphic_identity": RequirementType.TRANSPORT_UNLOCK,
    }

    def is_satisfied(self, account: "AccountProgress") -> bool:
        return account.has_transport_unlock(self.transport_id)


class BossKillCountRequirement(ActivityRequirement):
    __tablename__ = "boss_kill_count_requirements"

    id: Mapped[int] = mapped_column(ForeignKey("activity_requirements.id"), primary_key=True)
    boss_id: Mapped[uuid.UUID] = mapped_column(PG_UUID(as_uuid=True), nullable=False)
    kill_count: Mapped[int] = mapped_column(Integer, nullable=False)

    __mapper_args__ = {
        "polymorphic_identity": RequirementType.BOSS_KILL_COUNT,
    }

    def is_satisfied(self, account: "AccountProgress") -> bool:
        return account.boss_kill_count(self.boss_id) >= self.kill_count


class CombatLevelRequirement(ActivityRequirement):
    __tablename__ = "combat_level_requirements"

    id: Mapped[int] = mapped_column(ForeignKey("activity_requirements.id"), primary_key=True)
    minimum_level: Mapped[int] = mapped_column(Integer, nullable=False)

    __mapper_args__ = {
        "polymorphic_identity": RequirementType.COMBAT_LEVEL,
    }

    def is_satisfied(self, account: "AccountProgress") -> bool:
        return account.combat_level() >= self.minimum_level


class NecromancyTalentRequirement(ActivityRequirement):
    __tablename__ = "necromancy_talent_requirements"

    id: Mapped[int] = mapped_column(ForeignKey("activity_requirements.id"), primary_key=True)
    required_talent: Mapped[int] = mapped_column(Integer, nullable=False)

    __mapper_args__ = {
        "polymorphic_identity": RequirementType.NECROMANCY_TALENT,
    }

    def is_satisfied(self, account: "AccountProgress") -> bool:
        return account.necromancy_talent() >= self.required_talent


class CollectionLogRequirement(ActivityRequirement):
    __tablename__ = "collection_log_requirements"

    id: Mapped[int] = mapped_column(ForeignKey("activity_requirements.id"), primary_key=True)
    entry_id: Mapped[uuid.UUID] = mapped_column(PG_UUID(as_uuid=True), nullable=False)

    __mapper_args__ = {
        "polymorphic_identity": RequirementType.COLLECTION_LOG,
    }

    def is_satisfied(self, account: "AccountProgress") -> bool:
        return account.has_collection_log(self.entry_id)


class ArchaeologyMysteryRequirement(ActivityRequirement):
    __tablename__ = "archaeology_mystery_requirements"

    id: Mapped[int] = mapped_column(ForeignKey("activity_requirements.id"), primary_key=True)
    mystery_id: Mapped[uuid.UUID] = mapped_column(PG_UUID(as_uuid=True), nullable=False)

    __mapper_args__ = {
        "polymorphic_identity": RequirementType.ARCHAEOLOGY_MYSTERY,
    }

    def is_satisfied(self, account: "AccountProgress") -> bool:
        return account.archaeology_mystery(self.mystery_id)


class ResearchRequirement(ActivityRequirement):
    __tablename__ = "research_requirements"

    id: Mapped[int] = mapped_column(ForeignKey("activity_requirements.id"), primary_key=True)
    research_id: Mapped[uuid.UUID] = mapped_column(PG_UUID(as_uuid=True), nullable=False)

    __mapper_args__ = {
        "polymorphic_identity": RequirementType.RESEARCH,
    }

    def is_satisfied(self, account: "AccountProgress") -> bool:
        return account.has_research(self.research_id)


class PlayerOwnedFarmRequirement(ActivityRequirement):
    __tablename__ = "player_owned_farm_requirements"

    id: Mapped[int] = mapped_column(ForeignKey("activity_requirements.id"), primary_key=True)

    __mapper_args__ = {
        "polymorphic_identity": RequirementType.PLAYER_OWNED_FARM,
    }

    def is_satisfied(self, account: "AccountProgress") -> bool:
        return account.has_player_owned_farm()


class PortsProgressRequirement(ActivityRequirement):
    __tablename__ = "ports_progress_requirements"

    id: Mapped[int] = mapped_column(ForeignKey("activity_requirements.id"), primary_key=True)
    region_id: Mapped[uuid.UUID] = mapped_column(PG_UUID(as_uuid=True), nullable=False)

    __mapper_args__ = {
        "polymorphic_identity": RequirementType.PORTS_PROGRESS,
    }

    def is_satisfied(self, account: "AccountProgress") -> bool:
        return account.ports_progress(self.region_id)
