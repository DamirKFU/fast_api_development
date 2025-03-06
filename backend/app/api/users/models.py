import uuid

import pydantic
import sqlmodel


class User(sqlmodel.SQLModel, table=True):
    id: uuid.UUID = sqlmodel.Field(  # noqa: A003
        default_factory=uuid.uuid4,
        primary_key=True,
    )
    username: str = sqlmodel.Field(
        unique=True,
        index=True,
        max_length=52,
    )
    is_active: bool = sqlmodel.Field(default=True)
    email: pydantic.EmailStr = sqlmodel.Field(
        unique=True,
        index=True,
        max_length=255,
    )
    hashed_password: str
