from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .deps import get_repository
from ..db.session import get_db
from ..repositories.activity import ActivityRepository
from ..schemas.recommendation import RecommendationResponse
from ..services.recommendation import RecommendationService

router = APIRouter()


@router.get("/recommendation", response_model=RecommendationResponse)
def get_recommendation(db: Session = Depends(get_db)) -> RecommendationResponse:
    repository = get_repository(ActivityRepository, db)
    service = RecommendationService(repository)
    recommendation = service.recommend()
    return {"recommendation": recommendation}
