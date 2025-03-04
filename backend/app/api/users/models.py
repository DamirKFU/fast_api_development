import uuid

import sqlmodel


class User(sqlmodel.SQLModel, table=True):
    id: uuid.UUID = sqlmodel.Field(  # noqa: A003
        default_factory=uuid.uuid4, primary_key=True
    )
    username: str
    is_active: bool = sqlmodel.Field(default=True)
