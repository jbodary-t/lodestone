from typing import Iterable
from sqlalchemy.orm import Session
from ..models.account import Account
from ..db.base import BaseRepository
from ..schemas.account import AccountCreate


class AccountRepository(BaseRepository):
    def get_by_id(self, account_id: int) -> Account | None:
        return self.session.get(Account, account_id)

    def get_by_email(self, email: str) -> Account | None:
        return self.session.query(Account).filter_by(email=email).first()

    def list(self) -> Iterable[Account]:
        return self.session.query(Account).order_by(Account.id).all()

    def create(self, account_in: AccountCreate, hashed_password: str) -> Account:
        account = Account(
            email=account_in.email,
            hashed_password=hashed_password,
            full_name=account_in.full_name,
        )
        return self.add(account)
