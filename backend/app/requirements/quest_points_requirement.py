from __future__ import annotations

from pydantic import Field
from .base import Requirement, RequirementType


class QuestPointsRequirement(Requirement):
    type: RequirementType = Field(default=RequirementType.QUEST_POINTS, const=True)
    minimum_points: int

    def is_satisfied(self, account: "AccountProgress") -> bool:
        return account.quest_points() >= self.minimum_points
