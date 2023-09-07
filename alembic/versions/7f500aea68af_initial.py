"""initial

Revision ID: 7f500aea68af
Revises: 6e9814688214
Create Date: 2023-09-07 22:19:58.221269

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7f500aea68af'
down_revision: Union[str, None] = '6e9814688214'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
