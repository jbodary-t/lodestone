from __future__ import annotations

import uuid
from pydantic import Field
from .base import Requirement, RequirementType


class QuestRequirement(Requirement):
    type: RequirementType = Field(default=RequirementType.QUEST, const=True)
    quest_id: uuid.UUID

    def is_satisfied(self, account: "AccountProgress") -> bool:
        return account.has_completed_quest(self.quest_id)
