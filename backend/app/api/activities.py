from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..db.session import get_db
from .deps import get_repository
from ..repositories.activity import ActivityRepository
from ..schemas.activity import ActivityCreate, ActivityRead, ActivityUpdate
from ..services.activity import ActivityService

router = APIRouter()


@router.post("/", response_model=ActivityRead, status_code=status.HTTP_201_CREATED)
def create_activity(*, activity_in: ActivityCreate, db: Session = Depends(get_db)) -> ActivityRead:
    activity_repo = get_repository(ActivityRepository, db)
    service = ActivityService(activity_repo)
    activity = service.create_activity(activity_in)
    return activity


@router.get("/{activity_id}", response_model=ActivityRead)
def read_activity(*, activity_id: int, db: Session = Depends(get_db)) -> ActivityRead:
    activity_repo = get_repository(ActivityRepository, db)
    service = ActivityService(activity_repo)
    activity = service.get_activity_by_id(activity_id)
    if activity is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Activity not found")
    return activity


@router.patch("/{activity_id}", response_model=ActivityRead)
def update_activity(*, activity_id: int, activity_in: ActivityUpdate, db: Session = Depends(get_db)) -> ActivityRead:
    activity_repo = get_repository(ActivityRepository, db)
    service = ActivityService(activity_repo)
    activity = service.update_activity(activity_id, activity_in)
    if activity is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Activity not found")
    return activity


@router.delete("/{activity_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_activity(*, activity_id: int, db: Session = Depends(get_db)) -> None:
    activity_repo = get_repository(ActivityRepository, db)
    service = ActivityService(activity_repo)
    deleted = service.delete_activity(activity_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Activity not found")
