from typing import Iterator
from sqlalchemy.orm import Session


class BaseRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def add(self, instance: object) -> object:
        self.session.add(instance)
        self.session.commit()
        self.session.refresh(instance)
        return instance

    def delete(self, instance: object) -> None:
        self.session.delete(instance)
        self.session.commit()

    def refresh(self, instance: object) -> object:
        self.session.refresh(instance)
        return instance

    def flush(self) -> None:
        self.session.flush()
