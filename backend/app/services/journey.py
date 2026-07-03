import uuid
from typing import Iterable

from ..models.journey import Journey, JourneyType
from ..repositories.journey import JourneyRepository
from ..schemas.journey import JourneyCreate, JourneyRead, JourneyUpdate


class JourneyService:
    def __init__(self, repository: JourneyRepository) -> None:
        self.repository = repository

    def list_journeys(self, account_id: int | None = None) -> list[Journey]:
        return list(self.repository.list(account_id=account_id))

    def get_journey_by_id(self, journey_id: uuid.UUID) -> Journey | None:
        return self.repository.get_by_id(journey_id)

    def create_journey(self, journey_in: JourneyCreate) -> Journey:
        validated = self._validate_journey_data(journey_in)
        return self.repository.create(validated)

    def update_journey(self, journey_id: uuid.UUID, journey_in: JourneyUpdate) -> Journey | None:
        journey = self.repository.get_by_id(journey_id)
        if journey is None:
            return None
        validated = self._validate_journey_data(journey_in, existing_journey=journey)
        return self.repository.update(journey, validated)

    def delete_journey(self, journey_id: uuid.UUID) -> bool:
        journey = self.repository.get_by_id(journey_id)
        if journey is None:
            return False
        self.repository.delete(journey)
        return True

    def _validate_journey_data(self, journey_in: JourneyCreate | JourneyUpdate, existing_journey: Journey | None = None):
        if journey_in.preferences is not None:
            journey_in.preferences = self._unique_ordered([preference for preference in journey_in.preferences])
        if journey_in.constraints is not None:
            journey_in.constraints = self._unique_ordered([constraint for constraint in journey_in.constraints])

        if journey_in.starting_state is not None and not isinstance(journey_in.starting_state, dict):
            raise ValueError("Starting state must be a JSON object.")
        if journey_in.target_state is not None and not isinstance(journey_in.target_state, dict):
            raise ValueError("Target state must be a JSON object.")

        journey_type = journey_in.journey_type if hasattr(journey_in, "journey_type") else None
        target_state = journey_in.target_state if journey_in.target_state is not None else None
        if journey_type is None and existing_journey is not None:
            journey_type = existing_journey.journey_type
        if target_state is None and existing_journey is not None:
            target_state = existing_journey.target_state

        if journey_type is not None and journey_type != JourneyType.CUSTOM and not target_state:
            raise ValueError("Target state is required for non-custom journey types.")

        return journey_in

    @staticmethod
    def _unique_ordered(items: list) -> list:
        seen = set()
        unique_items = []
        for item in items:
            if item.value not in seen:
                seen.add(item.value)
                unique_items.append(item)
        return unique_items
