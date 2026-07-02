from __future__ import annotations

from pydantic import Field
from .base import Requirement, RequirementType


class PlayerOwnedFarmRequirement(Requirement):
    type: RequirementType = Field(default=RequirementType.PLAYER_OWNED_FARM, const=True)

    def is_satisfied(self, account: "AccountProgress") -> bool:
        return account.has_player_owned_farm()
