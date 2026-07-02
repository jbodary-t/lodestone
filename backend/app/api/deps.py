from typing import Type
from sqlalchemy.orm import Session

from ..db.base import BaseRepository


def get_repository(repository_class: Type[BaseRepository], db: Session) -> BaseRepository:
    return repository_class(db)
