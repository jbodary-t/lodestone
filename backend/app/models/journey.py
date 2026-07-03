import uuid
from datetime import datetime
from enum import StrEnum

from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer, JSON, String
from sqlalchemy.dialects.postgresql import UUID as PG_UUID

from .base import Base


class JourneyGame(StrEnum):
    RS3 = "RS3"
    OSRS = "OSRS"


class AccountType(StrEnum):
    STANDARD = "standard"
    IRONMAN = "ironman"
    HARDCORE_IRONMAN = "hardcore_ironman"
    ULTIMATE_IRONMAN = "ultimate_ironman"
    GROUP_IRONMAN = "group_ironman"


class JourneyType(StrEnum):
    TRIMMED_COMPLETIONIST = "trimmed_completionist"
    COMPLETIONIST = "completionist"
    MASTER_QUEST_CAPE = "master_quest_cape"
    QUEST_CAPE = "quest_cape"
    MAX_CAPE = "max_cape"
    SKILL_GOAL = "skill_goal"
    BOSS_GOAL = "boss_goal"
    COLLECTION_LOG = "collection_log"
    CUSTOM = "custom"


class OptimizationMode(StrEnum):
    EXPLORER = "explorer"
    PATHFINDER = "pathfinder"
    NAVIGATOR = "navigator"
    CUSTOM = "custom"


class JourneyPreference(StrEnum):
    AFK = "afk"
    MINIMIZE_DAILIES = "minimize_dailies"
    MINIMIZE_COST = "minimize_cost"
    IRONMAN_FRIENDLY = "ironman_friendly"
    COLLECTION_LOG_FOCUS = "collection_log_focus"
    LORE_FOCUS = "lore_focus"
    PVM_FOCUS = "pvm_focus"
    SKILLING_FOCUS = "skilling_focus"
    ACCESSIBILITY = "accessibility"


class JourneyConstraint(StrEnum):
    AVOID_BOSSING = "avoid_bossing"
    LIMIT_DAILIES = "limit_dailies"
    MAX_COST = "max_cost"
    REQUIRE_IRONMAN_FRIENDLY = "require_ironman_friendly"
    NO_MEMBER_CONTENT = "no_member_content"
    PREFERRED_SKILLING = "preferred_skilting"
    TRAVEL_MINIMIZATION = "travel_minimization"


class JourneyStatus(StrEnum):
    DRAFT = "draft"
    ACTIVE = "active"
    PAUSED = "paused"
    COMPLETED = "completed"
    ARCHIVED = "archived"


class Journey(Base):
    __tablename__ = "journeys"

    id = Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    account_id = Column(Integer, ForeignKey("accounts.id"), nullable=False, index=True)
    name = Column(String(length=200), nullable=False)
    description = Column(String(length=1000), nullable=True)
    game = Column(Enum(JourneyGame, name="journey_game", native_enum=False), nullable=False)
    account_type = Column(Enum(AccountType, name="account_type", native_enum=False), nullable=False)
    journey_type = Column(Enum(JourneyType, name="journey_type", native_enum=False), nullable=False)
    optimization_mode = Column(Enum(OptimizationMode, name="journey_optimization_mode", native_enum=False), nullable=False)
    preferences = Column(JSON, nullable=False, default=list)
    constraints = Column(JSON, nullable=False, default=list)
    starting_state = Column(JSON, nullable=False, default=dict)
    target_state = Column(JSON, nullable=False, default=dict)
    status = Column(Enum(JourneyStatus, name="journey_status", native_enum=False), nullable=False, default=JourneyStatus.DRAFT)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
