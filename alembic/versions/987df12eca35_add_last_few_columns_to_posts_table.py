"""add last few columns to posts table

Revision ID: 987df12eca35
Revises: e7d2aae9fa6f
Create Date: 2023-03-30 22:48:27.107020

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '987df12eca35'
down_revision = 'e7d2aae9fa6f'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(),
                  nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(
        timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
