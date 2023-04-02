"""add content column to posts table

Revision ID: 30e856712f15
Revises: e585ed736f72
Create Date: 2023-03-30 19:57:47.833005

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '30e856712f15'
down_revision = 'e585ed736f72'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
