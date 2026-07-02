from typing import Iterable
from sqlalchemy.orm import Session
from ..models.skill import Skill
from ..db.base import BaseRepository
from ..schemas.activity import ActivityCreate


class SkillRepository(BaseRepository):
    def get_by_id(self, skill_id: int) -> Skill | None:
        return self.session.get(Skill, skill_id)

    def list(self) -> Iterable[Skill]:
        return self.session.query(Skill).order_by(Skill.id).all()

    def create(self, activity_in: ActivityCreate) -> Skill:
        skill = Skill(
            title=activity_in.title,
            description=activity_in.description,
            owner_email=activity_in.owner_email,
            status=activity_in.status,
            domain="general",
            level=1,
        )
        return self.add(skill)
