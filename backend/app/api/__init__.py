from fastapi import APIRouter
from . import accounts, activities, health, recommendation


api_router = APIRouter()
api_router.include_router(accounts.router, prefix="/accounts", tags=["accounts"])
api_router.include_router(activities.router, prefix="/activities", tags=["activities"])
api_router.include_router(health.router, tags=["health"])
api_router.include_router(recommendation.router, tags=["recommendation"])
