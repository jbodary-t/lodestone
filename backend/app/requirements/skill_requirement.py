from __future__ import annotations

import uuid
from pydantic import Field
from .base import Requirement, RequirementType


class SkillRequirement(Requirement):
    type: RequirementType = Field(default=RequirementType.SKILL, const=True)
    skill: str
    level: int

    def is_satisfied(self, account: "AccountProgress") -> bool:
        return account.has_skill(self.skill, self.level)
