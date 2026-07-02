from ..repositories.activity import ActivityRepository
from ..schemas.activity import ActivityCreate, ActivityUpdate
from ..models.activity import Activity


class ActivityService:
    def __init__(self, repository: ActivityRepository) -> None:
        self.repository = repository

    def create_activity(self, activity_in: ActivityCreate) -> Activity:
        return self.repository.create(activity_in)

    def get_activity_by_id(self, activity_id: int) -> Activity | None:
        return self.repository.get_by_id(activity_id)

    def update_activity(self, activity_id: int, activity_in: ActivityUpdate) -> Activity | None:
        activity = self.repository.get_by_id(activity_id)
        if activity is None:
            return None
        return self.repository.update(activity, activity_in)

    def delete_activity(self, activity_id: int) -> bool:
        activity = self.repository.get_by_id(activity_id)
        if activity is None:
            return False
        self.repository.delete(activity)
        return True
