import uuid
from typing import Iterable

from sqlalchemy.orm import Session

from ..db.base import BaseRepository
from ..models.journey import Journey
from ..schemas.journey import JourneyCreate, JourneyUpdate


class JourneyRepository(BaseRepository):
    def get_by_id(self, journey_id: uuid.UUID) -> Journey | None:
        return self.session.get(Journey, journey_id)

    def list(self, account_id: int | None = None) -> Iterable[Journey]:
        query = self.session.query(Journey).order_by(Journey.created_at)
        if account_id is not None:
            query = query.filter_by(account_id=account_id)
        return query.all()

    def create(self, journey_in: JourneyCreate) -> Journey:
        journey = Journey(
            account_id=journey_in.account_id,
            name=journey_in.name,
            description=journey_in.description,
            game=journey_in.game,
            account_type=journey_in.account_type,
            journey_type=journey_in.journey_type,
            optimization_mode=journey_in.optimization_mode,
            preferences=[preference.value for preference in journey_in.preferences],
            constraints=[constraint.value for constraint in journey_in.constraints],
            starting_state=journey_in.starting_state,
            target_state=journey_in.target_state,
        )
        return self.add(journey)

    def update(self, journey: Journey, journey_in: JourneyUpdate) -> Journey:
        if journey_in.name is not None:
            journey.name = journey_in.name
        if journey_in.description is not None:
            journey.description = journey_in.description
        if journey_in.game is not None:
            journey.game = journey_in.game
        if journey_in.account_type is not None:
            journey.account_type = journey_in.account_type
        if journey_in.journey_type is not None:
            journey.journey_type = journey_in.journey_type
        if journey_in.optimization_mode is not None:
            journey.optimization_mode = journey_in.optimization_mode
        if journey_in.preferences is not None:
            journey.preferences = [preference.value for preference in journey_in.preferences]
        if journey_in.constraints is not None:
            journey.constraints = [constraint.value for constraint in journey_in.constraints]
        if journey_in.starting_state is not None:
            journey.starting_state = journey_in.starting_state
        if journey_in.target_state is not None:
            journey.target_state = journey_in.target_state
        if journey_in.status is not None:
            journey.status = journey_in.status
        self.session.commit()
        self.session.refresh(journey)
        return journey

    def delete(self, journey: Journey) -> None:
        self.session.delete(journey)
        self.session.commit()
