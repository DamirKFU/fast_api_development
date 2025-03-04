import logging

import sqlalchemy
import sqlmodel
import tenacity
import uvicorn

import app.core.config
import app.core.db

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

max_tries = 60 * 5
wait_seconds = 1


@tenacity.retry(
    stop=tenacity.stop_after_attempt(max_tries),
    wait=tenacity.wait_fixed(wait_seconds),
    before=tenacity.before_log(logger, logging.INFO),
    after=tenacity.after_log(logger, logging.WARN),
)
def init(db_engine: sqlalchemy.Engine) -> None:
    try:
        with sqlmodel.Session(db_engine) as session:
            session.exec(sqlmodel.select(1))
    except Exception as e:
        logger.error(e)
        raise e


def main() -> None:
    logger.info("Initializing service")
    init(app.core.db.engine)
    logger.info("Service finished initializing")
    uvicorn.run(
        "server:asgi_app",
        host=app.core.config.settings.HOST,
        port=app.core.config.settings.PORT,
        reload=True,
    )


if __name__ == "__main__":
    main()
