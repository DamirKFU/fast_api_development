import sqlmodel


class User(sqlmodel.SQLModel, table=True):
    id: int | None = sqlmodel.Field(  # noqa: A003
        default=None, primary_key=True
    )
    username: str
    is_active: bool = sqlmodel.Field(default=True)
