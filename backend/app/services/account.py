from ..repositories.account import AccountRepository
from ..schemas.account import AccountCreate
from ..models.account import Account
from ..core.security import hash_password


class AccountService:
    def __init__(self, repository: AccountRepository) -> None:
        self.repository = repository

    def create_account(self, account_in: AccountCreate) -> Account:
        existing = self.repository.get_by_email(account_in.email)
        if existing is not None:
            raise ValueError("Account with this email already exists.")

        hashed_password = hash_password(account_in.password)
        return self.repository.create(account_in, hashed_password)

    def get_account_by_id(self, account_id: int) -> Account | None:
        return self.repository.get_by_id(account_id)
