import uuid

import pydantic
import sqlmodel


class UserBase(sqlmodel.SQLModel):
    email: pydantic.EmailStr = sqlmodel.Field(
        unique=True, index=True, max_length=255
    )
    is_active: bool = True
    is_superuser: bool = False
    full_name: str | None = sqlmodel.Field(default=None, max_length=255)


class User(UserBase, table=True):
    id: uuid.UUID = sqlmodel.Field(  # noqa: A003
        default_factory=uuid.uuid4, primary_key=True
    )
    hashed_password: str
