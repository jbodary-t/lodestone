from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..db.session import get_db
from ..models.account import Account
from ..schemas.account import AccountCreate, AccountRead
from .deps import get_repository
from ..repositories.account import AccountRepository
from ..services.account import AccountService

router = APIRouter()


@router.post("/", response_model=AccountRead, status_code=status.HTTP_201_CREATED)
def create_account(*, account_in: AccountCreate, db: Session = Depends(get_db)) -> Account:
    account_repo = get_repository(AccountRepository, db)
    service = AccountService(account_repo)
    account = service.create_account(account_in)
    return account


@router.get("/{account_id}", response_model=AccountRead)
def read_account(*, account_id: int, db: Session = Depends(get_db)) -> Account:
    account_repo = get_repository(AccountRepository, db)
    service = AccountService(account_repo)
    account = service.get_account_by_id(account_id)
    if account is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Account not found")
    return account
