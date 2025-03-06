import os
import pathlib
import secrets

import pydantic
import pydantic_core
import pydantic_settings


def clear_env() -> None:
    try:
        with pathlib.Path("../.env").open("r") as f:
            for line in f:
                line = line.strip().split("=")[0]
                if line in os.environ:
                    del os.environ[line]
    except FileNotFoundError:
        pass


class Settings(pydantic_settings.BaseSettings):
    clear_env()
    model_config = pydantic_settings.SettingsConfigDict(
        env_file="../.env",
        env_ignore_empty=True,
        extra="ignore",
    )
    PROJECT_NAME: str = "backend"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    HOST: str = "localhost"
    PORT: int = 8000
    DEBUG: bool = True

    POSTGRES_SERVER: str
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str = ""
    POSTGRES_DB: str = ""

    @pydantic.computed_field  # type: ignore[prop-decorator]
    @property
    def sqlalchemy_database_uri(self) -> pydantic_core.MultiHostUrl:
        return pydantic_core.MultiHostUrl.build(
            scheme="postgresql+psycopg",
            username=self.POSTGRES_USER,
            password=self.POSTGRES_PASSWORD,
            host=self.POSTGRES_SERVER,
            port=self.POSTGRES_PORT,
            path=self.POSTGRES_DB,
        )


settings = Settings()  # type: ignore
