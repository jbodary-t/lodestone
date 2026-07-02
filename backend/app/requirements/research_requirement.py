from __future__ import annotations

import uuid
from pydantic import Field
from .base import Requirement, RequirementType


class ResearchRequirement(Requirement):
    type: RequirementType = Field(default=RequirementType.RESEARCH, const=True)
    research_id: uuid.UUID

    def is_satisfied(self, account: "AccountProgress") -> bool:
        return account.has_research(self.research_id)
