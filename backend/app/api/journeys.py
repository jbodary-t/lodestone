import uuid
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .deps import get_repository
from ..db.session import get_db
from ..repositories.journey import JourneyRepository
from ..schemas.journey import JourneyCreate, JourneyRead, JourneyUpdate
from ..services.journey import JourneyService

router = APIRouter()


@router.post("/", response_model=JourneyRead, status_code=status.HTTP_201_CREATED)
def create_journey(*, journey_in: JourneyCreate, db: Session = Depends(get_db)) -> JourneyRead:
    repository = get_repository(JourneyRepository, db)
    service = JourneyService(repository)
    journey = service.create_journey(journey_in)
    return journey


@router.get("/", response_model=list[JourneyRead])
def list_journeys(*, account_id: int | None = None, db: Session = Depends(get_db)) -> list[JourneyRead]:
    repository = get_repository(JourneyRepository, db)
    service = JourneyService(repository)
    return service.list_journeys(account_id=account_id)


@router.get("/{journey_id}", response_model=JourneyRead)
def get_journey(*, journey_id: uuid.UUID, db: Session = Depends(get_db)) -> JourneyRead:
    repository = get_repository(JourneyRepository, db)
    service = JourneyService(repository)
    journey = service.get_journey_by_id(journey_id)
    if journey is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Journey not found")
    return journey


@router.patch("/{journey_id}", response_model=JourneyRead)
def update_journey(*, journey_id: uuid.UUID, journey_in: JourneyUpdate, db: Session = Depends(get_db)) -> JourneyRead:
    repository = get_repository(JourneyRepository, db)
    service = JourneyService(repository)
    journey = service.update_journey(journey_id, journey_in)
    if journey is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Journey not found")
    return journey


@router.delete("/{journey_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_journey(*, journey_id: uuid.UUID, db: Session = Depends(get_db)) -> None:
    repository = get_repository(JourneyRepository, db)
    service = JourneyService(repository)
    deleted = service.delete_journey(journey_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Journey not found")
