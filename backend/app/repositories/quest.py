from typing import Iterable
from sqlalchemy.orm import Session
from ..models.quest import Quest
from ..db.base import BaseRepository
from ..schemas.activity import ActivityCreate


class QuestRepository(BaseRepository):
    def get_by_id(self, quest_id: int) -> Quest | None:
        return self.session.get(Quest, quest_id)

    def list(self) -> Iterable[Quest]:
        return self.session.query(Quest).order_by(Quest.id).all()

    def create(self, activity_in: ActivityCreate) -> Quest:
        quest = Quest(
            title=activity_in.title,
            description=activity_in.description,
            owner_email=activity_in.owner_email,
            status=activity_in.status,
            quest_line="main path",
            difficulty="medium",
        )
        return self.add(quest)
