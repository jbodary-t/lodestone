from __future__ import annotations

import uuid
from pydantic import Field
from .base import Requirement, RequirementType


class DiaryRequirement(Requirement):
    type: RequirementType = Field(default=RequirementType.DIARY, const=True)
    diary_id: uuid.UUID

    def is_satisfied(self, account: "AccountProgress") -> bool:
        return account.has_diary(self.diary_id)
