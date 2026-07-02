from __future__ import annotations

import uuid
from pydantic import Field
from .base import Requirement, RequirementType


class ArchaeologyMysteryRequirement(Requirement):
    type: RequirementType = Field(default=RequirementType.ARCHAEOLOGY_MYSTERY, const=True)
    mystery_id: uuid.UUID

    def is_satisfied(self, account: "AccountProgress") -> bool:
        return account.archaeology_mystery(self.mystery_id)
