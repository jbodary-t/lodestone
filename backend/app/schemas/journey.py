import uuid
from enum import StrEnum
from typing import Any

from pydantic import BaseModel, Field, Json


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


class JourneyBase(BaseModel):
    account_id: int
    name: str = Field(..., max_length=200)
    description: str | None = Field(None, max_length=1000)
    game: JourneyGame
    account_type: AccountType
    journey_type: JourneyType
    optimization_mode: OptimizationMode
    preferences: list[JourneyPreference] = Field(default_factory=list)
    constraints: list[JourneyConstraint] = Field(default_factory=list)
    starting_state: dict[str, Any] = Field(default_factory=dict)
    target_state: dict[str, Any] = Field(default_factory=dict)


class JourneyCreate(JourneyBase):
    pass


class JourneyUpdate(BaseModel):
    name: str | None = Field(None, max_length=200)
    description: str | None = Field(None, max_length=1000)
    game: JourneyGame | None = None
    account_type: AccountType | None = None
    journey_type: JourneyType | None = None
    optimization_mode: OptimizationMode | None = None
    preferences: list[JourneyPreference] | None = None
    constraints: list[JourneyConstraint] | None = None
    starting_state: dict[str, Any] | None = None
    target_state: dict[str, Any] | None = None
    status: str | None = None


class JourneyRead(JourneyBase):
    id: uuid.UUID
    status: str
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True,
    }
