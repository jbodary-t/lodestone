from __future__ import annotations

from pydantic import Field
from .base import Requirement, RequirementType


class CombatLevelRequirement(Requirement):
    type: RequirementType = Field(default=RequirementType.COMBAT_LEVEL, const=True)
    minimum_level: int

    def is_satisfied(self, account: "AccountProgress") -> bool:
        return account.combat_level() >= self.minimum_level
