from __future__ import annotations

import uuid
from pydantic import Field
from .base import Requirement, RequirementType


class CollectionLogRequirement(Requirement):
    type: RequirementType = Field(default=RequirementType.COLLECTION_LOG, const=True)
    entry_id: uuid.UUID

    def is_satisfied(self, account: "AccountProgress") -> bool:
        return account.has_collection_log(self.entry_id)
