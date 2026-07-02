from datetime import datetime

from fastapi import APIRouter
from ..core.config import settings

router = APIRouter()
APPLICATION_START_TIME = datetime.utcnow()


@router.get("/health")
def health_check() -> dict[str, str]:
    uptime_seconds = int((datetime.utcnow() - APPLICATION_START_TIME).total_seconds())
    return {
        "status": "ok",
        "project": settings.PROJECT_NAME,
        "version": settings.PROJECT_VERSION,
        "uptime": f"{uptime_seconds} seconds",
    }
