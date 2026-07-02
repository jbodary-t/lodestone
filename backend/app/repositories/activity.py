from typing import Iterable
from sqlalchemy.orm import Session
from ..models.activity import Activity
from ..db.base import BaseRepository
from ..schemas.activity import ActivityCreate, ActivityUpdate


class ActivityRepository(BaseRepository):
    def get_by_id(self, activity_id: int) -> Activity | None:
        return self.session.get(Activity, activity_id)

    def list(self) -> Iterable[Activity]:
        return self.session.query(Activity).order_by(Activity.id).all()

    def create(self, activity_in: ActivityCreate) -> Activity:
        activity = Activity(
            title=activity_in.title,
            description=activity_in.description,
            owner_email=activity_in.owner_email,
            status=activity_in.status,
        )
        return self.add(activity)

    def update(self, activity: Activity, activity_in: ActivityUpdate) -> Activity:
        if activity_in.title is not None:
            activity.title = activity_in.title
        if activity_in.description is not None:
            activity.description = activity_in.description
        if activity_in.status is not None:
            activity.status = activity_in.status
        self.session.commit()
        self.session.refresh(activity)
        return activity

    def delete(self, activity: Activity) -> None:
        self.session.delete(activity)
        self.session.commit()
