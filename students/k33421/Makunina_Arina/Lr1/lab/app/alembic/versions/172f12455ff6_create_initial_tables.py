"""Create initial tables

Revision ID: 172f12455ff6
Revises: 90e653515401
Create Date: 2024-03-16 17:45:54.588868

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel
from datetime import datetime


# revision identifiers, used by Alembic.
revision: str = "172f12455ff6"
down_revision: Union[str, None] = "90e653515401"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
