from __future__ import annotations

import uuid
from pydantic import Field
from .base import Requirement, RequirementType


class TransportUnlockRequirement(Requirement):
    type: RequirementType = Field(default=RequirementType.TRANSPORT_UNLOCK, const=True)
    transport_id: uuid.UUID

    def is_satisfied(self, account: "AccountProgress") -> bool:
        return account.has_transport_unlock(self.transport_id)
