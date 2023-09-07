"""create_database

Revision ID: 10b90610f641
Revises: 
Create Date: 2023-09-07 04:24:34.653478

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '10b90610f641'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade():
    from alembic import op
    from lib.config import DATABASE_URL

    # Create the initial database if it doesn't exist
    op.execute(f"CREATE DATABASE IF NOT EXISTS {DATABASE_URL.split('/')[-1]}")



def downgrade() -> None:
    pass
