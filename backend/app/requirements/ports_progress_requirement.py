from __future__ import annotations

import uuid
from pydantic import Field
from .base import Requirement, RequirementType


class PortsProgressRequirement(Requirement):
    type: RequirementType = Field(default=RequirementType.PORTS_PROGRESS, const=True)
    region_id: uuid.UUID

    def is_satisfied(self, account: "AccountProgress") -> bool:
        return account.ports_progress(self.region_id)
