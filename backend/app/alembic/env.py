from logging.config import fileConfig
from pathlib import Path
from importlib import import_module
from inspect import isclass, getmembers
import sqlmodel

from sqlalchemy import engine_from_config
from sqlalchemy import pool
from app.core.config import settings  # noqa
from alembic import context

def import_models_from_api():
    api_path = Path("./app/api").resolve() 
    models = []

    for module_dir in api_path.iterdir():
        if not module_dir.is_dir():
            continue

        models_file = module_dir / "models.py"
        if not models_file.exists():
            continue
            
        try:
            module_path = f"app.api.{module_dir.name}.models"
            module = import_module(module_path)
            
            for _, obj in getmembers(module):
                if (isclass(obj) and 
                    issubclass(obj, sqlmodel.SQLModel) and 
                    obj != sqlmodel.SQLModel):
                    models.append(obj)
                    print(f"Найдена модель: {obj.__name__} в {module_path}")
                    
        except ImportError as e:
            print(f"Не удалось импортировать {module_path}: {e}")
            
    return models

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.

config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
from app.core.config import settings  # noqa

target_metadata = sqlmodel.SQLModel.metadata

import_models_from_api()

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def get_url():
    return str(settings.sqlalchemy_database_uri)


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = get_url()
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    configuration = config.get_section(config.config_ini_section)
    configuration["sqlalchemy.url"] = get_url()
    connectable = engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
