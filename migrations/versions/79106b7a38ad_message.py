"""message

Revision ID: 79106b7a38ad
Revises: 62e4e3519983
Create Date: 2025-06-03 21:21:51.629801

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '79106b7a38ad'
down_revision: Union[str, None] = '62e4e3519983'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('passangers', 'Vehicle_type')
    op.drop_column('passangers', 'No_plate')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('passangers', sa.Column('No_plate', sa.TEXT(), nullable=True))
    op.add_column('passangers', sa.Column('Vehicle_type', sa.TEXT(), nullable=True))
    # ### end Alembic commands ###
