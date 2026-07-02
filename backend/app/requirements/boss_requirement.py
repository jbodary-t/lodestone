from __future__ import annotations

import uuid
from pydantic import Field
from .base import Requirement, RequirementType


class BossRequirement(Requirement):
    type: RequirementType = Field(default=RequirementType.BOSS_KILL_COUNT, const=True)
    boss_id: uuid.UUID
    kill_count: int

    def is_satisfied(self, account: "AccountProgress") -> bool:
        return account.boss_kill_count(self.boss_id) >= self.kill_count
