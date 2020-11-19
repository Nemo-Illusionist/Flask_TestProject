"""add can_review_tasks in user table

Revision ID: 72adadb46cc4
Revises: f97a73963d8a
Create Date: 2020-11-19 07:22:25.863958+00:00

"""
import sqlalchemy as sa
from alembic import op

revision = '72adadb46cc4'
down_revision = 'f97a73963d8a'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('user', sa.Column('can_review_tasks', sa.Boolean(), nullable=False, default=True))


def downgrade():
    op.drop_column('user', 'can_review_tasks')
