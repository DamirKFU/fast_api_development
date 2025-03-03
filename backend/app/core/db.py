import sqlmodel

import app.core.config


engine = sqlmodel.create_engine(
    str(app.core.config.settings.sqlalchemy_database_uri)
)


def init_db(session: sqlmodel.Session) -> None:
    pass
