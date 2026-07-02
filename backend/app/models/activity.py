from __future__ import annotations

import uuid
from datetime import datetime
from enum import StrEnum
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Enum,
    Float,
    ForeignKey,
    Integer,
    String,
    Table,
    Text,
)
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


class ActivityGame(StrEnum):
    RS3 = "RS3"
    OSRS = "OSRS"


class ActivityCategory(StrEnum):
    QUEST = "quest"
    BOSS = "boss"
    SKILL = "skill"
    DIARY = "diary"
    ACHIEVEMENT = "achievement"
    TRANSPORT = "transport"
    DAILY = "daily"
    MINIGAME = "minigame"
    COLLECTION = "collection"


class ActivityOutcomeKind(StrEnum):
    REWARD = "reward"
    UNLOCK = "unlock"


class ResourceDirection(StrEnum):
    INPUT = "input"
    OUTPUT = "output"


activity_tag_link = Table(
    "activity_tag_link",
    Base.metadata,
    Column("activity_id", PG_UUID(as_uuid=True), ForeignKey("activities.id"), primary_key=True),
    Column("tag_id", PG_UUID(as_uuid=True), ForeignKey("activity_tags.id"), primary_key=True),
)


activity_parent_child = Table(
    "activity_parent_child",
    Base.metadata,
    Column("parent_id", PG_UUID(as_uuid=True), ForeignKey("activities.id"), primary_key=True),
    Column("child_id", PG_UUID(as_uuid=True), ForeignKey("activities.id"), primary_key=True),
)


class Activity(Base):
    __tablename__ = "activities"

    id: Mapped[uuid.UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True,
    )
    name: Mapped[str] = mapped_column(String(length=200), nullable=False, index=True)
    game: Mapped[ActivityGame] = mapped_column(
        Enum(ActivityGame, name="activity_game", native_enum=False), nullable=False
    )
    category: Mapped[ActivityCategory] = mapped_column(
        Enum(ActivityCategory, name="activity_category", native_enum=False), nullable=False
    )
    estimated_minutes: Mapped[int] = mapped_column(nullable=False, default=0)
    repeatable: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    time_gated: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    wiki_url: Mapped[str | None] = mapped_column(String(length=400), nullable=True)
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
    )
    type: Mapped[str] = mapped_column(String(length=50), nullable=False, default="activity")

    tags = relationship(
        "ActivityTag",
        secondary=activity_tag_link,
        back_populates="activities",
        lazy="selectin",
    )
    requirements = relationship(
        "ActivityRequirement",
        back_populates="activity",
        cascade="all, delete-orphan",
        lazy="selectin",
    )
    outcomes = relationship(
        "ActivityOutcome",
        back_populates="activity",
        cascade="all, delete-orphan",
        lazy="selectin",
    )
    rewards = relationship(
        "ActivityOutcome",
        primaryjoin="and_(Activity.id==ActivityOutcome.activity_id, ActivityOutcome.kind=='reward')",
        viewonly=True,
        lazy="selectin",
    )
    unlocks = relationship(
        "ActivityOutcome",
        primaryjoin="and_(Activity.id==ActivityOutcome.activity_id, ActivityOutcome.kind=='unlock')",
        viewonly=True,
        lazy="selectin",
    )
    resources = relationship(
        "ActivityResource",
        back_populates="activity",
        cascade="all, delete-orphan",
        lazy="selectin",
    )
    resource_inputs = relationship(
        "ActivityResource",
        primaryjoin="and_(Activity.id==ActivityResource.activity_id, ActivityResource.direction=='input')",
        viewonly=True,
        lazy="selectin",
    )
    resource_outputs = relationship(
        "ActivityResource",
        primaryjoin="and_(Activity.id==ActivityResource.activity_id, ActivityResource.direction=='output')",
        viewonly=True,
        lazy="selectin",
    )
    parents = relationship(
        "Activity",
        secondary=activity_parent_child,
        primaryjoin=id == activity_parent_child.c.child_id,
        secondaryjoin=id == activity_parent_child.c.parent_id,
        back_populates="children",
        lazy="selectin",
    )
    children = relationship(
        "Activity",
        secondary=activity_parent_child,
        primaryjoin=id == activity_parent_child.c.parent_id,
        secondaryjoin=id == activity_parent_child.c.child_id,
        back_populates="parents",
        lazy="selectin",
    )

    __mapper_args__ = {
        "polymorphic_on": type,
        "polymorphic_identity": "activity",
    }


class QuestActivity(Activity):
    __tablename__ = "quest_activities"

    id: Mapped[uuid.UUID] = mapped_column(
        PG_UUID(as_uuid=True), ForeignKey("activities.id"), primary_key=True
    )
    quest_points: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    series: Mapped[str | None] = mapped_column(String(length=200), nullable=True)
    difficulty: Mapped[str | None] = mapped_column(String(length=50), nullable=True)
    length: Mapped[str | None] = mapped_column(String(length=50), nullable=True)
    combat_required: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    recommended_combat_level: Mapped[int | None] = mapped_column(Integer, nullable=True)
    recommended_inventory: Mapped[str | None] = mapped_column(Text, nullable=True)
    recommended_gear: Mapped[str | None] = mapped_column(Text, nullable=True)
    dialogue_steps: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    puzzle_steps: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    walkthrough_steps: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    nearby_optimizations: Mapped[str | None] = mapped_column(Text, nullable=True)

    __mapper_args__ = {
        "polymorphic_identity": "quest",
    }


class BossActivity(Activity):
    __tablename__ = "boss_activities"

    id: Mapped[uuid.UUID] = mapped_column(
        PG_UUID(as_uuid=True), ForeignKey("activities.id"), primary_key=True
    )
    combat_level: Mapped[int] = mapped_column(Integer, nullable=False, default=1)
    mechanics: Mapped[str | None] = mapped_column(Text, nullable=True)
    expected_kill_time_minutes: Mapped[int | None] = mapped_column(Integer, nullable=True)
    expected_kc: Mapped[int | None] = mapped_column(Integer, nullable=True)
    recommended_gear: Mapped[str | None] = mapped_column(Text, nullable=True)
    recommended_inventory: Mapped[str | None] = mapped_column(Text, nullable=True)
    unique_drops: Mapped[str | None] = mapped_column(Text, nullable=True)
    collection_log_entries: Mapped[str | None] = mapped_column(Text, nullable=True)

    __mapper_args__ = {
        "polymorphic_identity": "boss",
    }


class AchievementActivity(Activity):
    __mapper_args__ = {
        "polymorphic_identity": "achievement",
    }


class SkillTrainingActivity(Activity):
    __mapper_args__ = {
        "polymorphic_identity": "skill",
    }


class DailyActivity(Activity):
    __mapper_args__ = {
        "polymorphic_identity": "daily",
    }


class TransportationActivity(Activity):
    __mapper_args__ = {
        "polymorphic_identity": "transport",
    }


class MinigameActivity(Activity):
    __mapper_args__ = {
        "polymorphic_identity": "minigame",
    }


class CollectionLogActivity(Activity):
    __mapper_args__ = {
        "polymorphic_identity": "collection",
    }


class ActivityTag(Base):
    __tablename__ = "activity_tags"

    id: Mapped[uuid.UUID] = mapped_column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(length=100), nullable=False, unique=True)
    activities = relationship(
        "Activity",
        secondary=activity_tag_link,
        back_populates="tags",
        lazy="selectin",
    )


class ActivityRequirement(Base):
    __tablename__ = "activity_requirements"

    id: Mapped[int] = mapped_column(primary_key=True)
    activity_id: Mapped[uuid.UUID] = mapped_column(
        PG_UUID(as_uuid=True), ForeignKey("activities.id"), nullable=False
    )
    description: Mapped[str] = mapped_column(String(length=400), nullable=False)
    required_activity_id: Mapped[uuid.UUID | None] = mapped_column(
        PG_UUID(as_uuid=True), ForeignKey("activities.id"), nullable=True
    )

    activity = relationship("Activity", back_populates="requirements", foreign_keys=[activity_id])
    required_activity = relationship(
        "Activity",
        remote_side=[Activity.id],
        foreign_keys=[required_activity_id],
        lazy="selectin",
    )


class ActivityOutcome(Base):
    __tablename__ = "activity_outcomes"

    id: Mapped[int] = mapped_column(primary_key=True)
    activity_id: Mapped[uuid.UUID] = mapped_column(
        PG_UUID(as_uuid=True), ForeignKey("activities.id"), nullable=False
    )
    kind: Mapped[ActivityOutcomeKind] = mapped_column(
        Enum(ActivityOutcomeKind, name="activity_outcome_kind", native_enum=False), nullable=False
    )
    name: Mapped[str] = mapped_column(String(length=200), nullable=False)
    details: Mapped[str | None] = mapped_column(String(length=400), nullable=True)

    activity = relationship("Activity", back_populates="outcomes")


class ActivityResource(Base):
    __tablename__ = "activity_resources"

    id: Mapped[int] = mapped_column(primary_key=True)
    activity_id: Mapped[uuid.UUID] = mapped_column(
        PG_UUID(as_uuid=True), ForeignKey("activities.id"), nullable=False
    )
    direction: Mapped[ResourceDirection] = mapped_column(
        Enum(ResourceDirection, name="resource_direction", native_enum=False), nullable=False
    )
    item: Mapped[str] = mapped_column(String(length=200), nullable=False)
    quantity: Mapped[float] = mapped_column(Float, nullable=False, default=1.0)
    unit: Mapped[str] = mapped_column(String(length=50), nullable=False, default="unit")
    note: Mapped[str | None] = mapped_column(String(length=300), nullable=True)

    activity = relationship("Activity", back_populates="resources")
