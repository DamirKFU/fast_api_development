import typing

import fastapi
import sqlmodel

import app.core.config


engine = sqlmodel.create_engine(
    str(app.core.config.settings.sqlalchemy_database_uri)
)


def init_db(session: sqlmodel.Session) -> None:
    pass


def get_db() -> typing.Generator[sqlmodel.Session, None, None]:
    with sqlmodel.Session(engine) as session:
        yield session


SessionDep = typing.Annotated[sqlmodel.Session, fastapi.Depends(get_db)]
