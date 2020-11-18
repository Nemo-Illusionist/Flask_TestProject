"""empty message

Revision ID: f16e3d22ca4d
Revises: 7d66f834bc9e
Create Date: 2020-11-17 21:51:49.674557

"""
from alembic import op
import sqlalchemy as sa


revision = 'f16e3d22ca4d'
down_revision = '7d66f834bc9e'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('user', sa.Column('can_review_tasks', sa.Boolean(), nullable=False, default=False))


def downgrade():
    op.drop_column('user', 'can_review_tasks')
