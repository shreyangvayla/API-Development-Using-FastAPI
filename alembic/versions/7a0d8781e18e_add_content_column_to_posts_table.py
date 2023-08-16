"""add content column to posts table

Revision ID: 7a0d8781e18e
Revises: 3cbe1848dbaa
Create Date: 2023-08-14 23:54:33.310042

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7a0d8781e18e'
down_revision: Union[str, None] = '3cbe1848dbaa'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
