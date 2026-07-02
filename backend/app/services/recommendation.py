from typing import Optional
from ..repositories.activity import ActivityRepository
from ..schemas.recommendation import Recommendation


class RecommendationService:
    def __init__(self, repository: ActivityRepository) -> None:
        self.repository = repository

    def recommend(self) -> Recommendation:
        activities = self.repository.list()
        next_activity = self._select_next_activity(activities)
        if next_activity is None:
            return Recommendation(
                title="No active activities",
                summary="All current activities are complete or there are none scheduled.",
                rationale="No pending work was detected in the activity backlog.",
            )

        return Recommendation(
            title="Focus on next activity",
            summary=f"Continue with '{next_activity.title}' to maintain momentum.",
            rationale=(
                "This activity is the next uncompleted step in your journey and keeps progress aligned "
                "with your current goal."
            ),
        )

    def _select_next_activity(self, activities: list) -> Optional[object]:
        for activity in activities:
            if activity.status in {"scheduled", "in_progress"}:
                return activity
        return activities[0] if activities else None
