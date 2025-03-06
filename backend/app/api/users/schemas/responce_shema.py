import uuid

import sqlmodel


class UserResponse(sqlmodel.SQLModel):
    id: uuid.UUID  # noqa: A003
