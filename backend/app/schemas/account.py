from datetime import datetime
from pydantic import BaseModel, EmailStr, Field


class AccountBase(BaseModel):
    email: EmailStr
    full_name: str | None = None


class AccountCreate(AccountBase):
    password: str = Field(..., min_length=8)


class AccountRead(AccountBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True,
    }
