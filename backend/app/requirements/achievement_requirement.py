from __future__ import annotations

import uuid
from pydantic import Field
from .base import Requirement, RequirementType


class AchievementRequirement(Requirement):
    type: RequirementType = Field(default=RequirementType.ACHIEVEMENT, const=True)
    achievement_id: uuid.UUID

    def is_satisfied(self, account: "AccountProgress") -> bool:
        return account.has_achievement(self.achievement_id)
