from __future__ import annotations

import uuid
from datetime import datetime
from enum import StrEnum
from pydantic import BaseModel, Field, HttpUrl, conint, confloat


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


class ResourceDirection(StrEnum):
    INPUT = "input"
    OUTPUT = "output"


class ActivityRequirement(BaseModel):
    description: str = Field(..., max_length=400)
    required_activity_id: uuid.UUID | None = None


class ActivityOutcome(BaseModel):
    name: str = Field(..., max_length=200)
    details: str | None = Field(None, max_length=400)


class ActivityResource(BaseModel):
    item: str = Field(..., max_length=200)
    quantity: confloat(ge=0) = 1.0
    unit: str = Field(default="unit", max_length=50)
    note: str | None = Field(None, max_length=300)


class ActivityBase(BaseModel):
    name: str = Field(..., max_length=200)
    game: ActivityGame
    category: ActivityCategory
    estimated_minutes: conint(ge=0) = 0
    repeatable: bool = False
    time_gated: bool = False
    description: str | None = None
    wiki_url: HttpUrl | None = None
    notes: str | None = Field(None, max_length=2000)
    requirements: list[ActivityRequirement] = Field(default_factory=list)
    rewards: list[ActivityOutcome] = Field(default_factory=list)
    unlocks: list[ActivityOutcome] = Field(default_factory=list)
    resource_inputs: list[ActivityResource] = Field(default_factory=list)
    resource_outputs: list[ActivityResource] = Field(default_factory=list)
    tags: list[str] = Field(default_factory=list)


class ActivityCreate(ActivityBase):
    pass


class ActivityUpdate(BaseModel):
    name: str | None = Field(None, max_length=200)
    game: ActivityGame | None = None
    category: ActivityCategory | None = None
    estimated_minutes: conint(ge=0) | None = None
    repeatable: bool | None = None
    time_gated: bool | None = None
    description: str | None = None
    wiki_url: HttpUrl | None = None
    notes: str | None = Field(None, max_length=2000)
    requirements: list[ActivityRequirement] | None = None
    rewards: list[ActivityOutcome] | None = None
    unlocks: list[ActivityOutcome] | None = None
    resource_inputs: list[ActivityResource] | None = None
    resource_outputs: list[ActivityResource] | None = None
    tags: list[str] | None = None


class ActivityRead(ActivityBase):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime
    parents: list[uuid.UUID] = Field(default_factory=list)
    children: list[uuid.UUID] = Field(default_factory=list)

    model_config = {
        "from_attributes": True,
    }
