from logging.config import fileConfig
from alembic import context
from sqlalchemy import engine_from_config, pool

# Load the Alembic-specific logging configuration
fileConfig('alembic_logging.ini')

# This is the Alembic Config object, which provides access to the values within the .ini file in use.
config = context.config

# Define the SQLAlchemy engine based on the configuration file.
connectable = engine_from_config(
    config.get_section(config.config_ini_section),
    prefix="sqlalchemy.",
    poolclass=pool.NullPool,
)

# Attach the engine to the Alembic context.
with connectable.connect() as connection:
    context.configure(
        connection=connection,
    )

    # Run the migrations.
    with context.begin_transaction():
        context.run_migrations()
