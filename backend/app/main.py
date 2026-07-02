from fastapi import FastAPI
from .api import api_router
from .core.config import settings
from .db.session import engine
from .models.base import Base


def create_app() -> FastAPI:
    Base.metadata.create_all(bind=engine)
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.PROJECT_VERSION,
        description=settings.PROJECT_DESCRIPTION,
    )
    app.include_router(api_router, prefix="/api")
    return app


app = create_app()
