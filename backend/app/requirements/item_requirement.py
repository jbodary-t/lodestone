from __future__ import annotations

import uuid
from pydantic import Field
from .base import Requirement, RequirementType


class ItemRequirement(Requirement):
    type: RequirementType = Field(default=RequirementType.ITEM, const=True)
    item_id: uuid.UUID
    quantity: int

    def is_satisfied(self, account: "AccountProgress") -> bool:
        return account.has_item(self.item_id, self.quantity)
