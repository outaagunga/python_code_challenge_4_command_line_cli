"""create_tables

Revision ID: 0eea51860d85
Revises: 10b90610f641
Create Date: 2023-09-07 04:29:21.844510

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0eea51860d85'
down_revision: Union[str, None] = '10b90610f641'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade():
    from alembic import op
    from lib.config import DATABASE_URL

    # Create the initial database if it doesn't exist
    op.execute(f"CREATE DATABASE IF NOT EXISTS {DATABASE_URL.split('/')[-1]}")



def downgrade() -> None:
    pass
