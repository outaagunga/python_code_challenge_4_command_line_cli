"""initial

Revision ID: 6e9814688214
Revises: 0eea51860d85
Create Date: 2023-09-07 22:12:10.567724

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6e9814688214'
down_revision: Union[str, None] = '0eea51860d85'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
