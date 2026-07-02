from __future__ import annotations

import uuid
from pydantic import Field
from .base import Requirement, RequirementType


class AreaRequirement(Requirement):
    type: RequirementType = Field(default=RequirementType.AREA_UNLOCK, const=True)
    area_id: uuid.UUID

    def is_satisfied(self, account: "AccountProgress") -> bool:
        return account.has_area_unlock(self.area_id)
