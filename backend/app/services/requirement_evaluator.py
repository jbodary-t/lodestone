from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable
import uuid
from ..requirements.base import AccountProgress, Requirement
from ..schemas.activity import ActivityRead


@dataclass(frozen=True)
class RequirementEvaluation:
    is_completed: bool
    failed_requirements: list[Requirement]
    completed_requirements: list[Requirement]
    missing_items: list[uuid.UUID]
    missing_skills: list[str]
    missing_quests: list[uuid.UUID]


class RequirementEvaluator:
    def evaluate(self, account: AccountProgress, activity: ActivityRead) -> RequirementEvaluation:
        completed: list[Requirement] = []
        failed: list[Requirement] = []
        missing_items: list[uuid.UUID] = []
        missing_skills: list[str] = []
        missing_quests: list[uuid.UUID] = []

        for requirement in activity.requirements:
            if requirement.is_satisfied(account):
                completed.append(requirement)
            else:
                failed.append(requirement)
                if requirement.type == requirement.Type.SKILL:
                    missing_skills.append(requirement.skill)
                elif requirement.type == requirement.Type.QUEST:
                    missing_quests.append(requirement.quest_id)
                elif requirement.type == requirement.Type.ITEM:
                    missing_items.append(requirement.item_id)

        return RequirementEvaluation(
            is_completed=not failed,
            failed_requirements=failed,
            completed_requirements=completed,
            missing_items=missing_items,
            missing_skills=missing_skills,
            missing_quests=missing_quests,
        )
