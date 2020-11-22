"""add TaskResults table

Revision ID: af1c94bed1a7
Revises: 72adadb46cc4
Create Date: 2020-11-21 21:15:22.666483+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'af1c94bed1a7'
down_revision = '72adadb46cc4'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('task_results',
    sa.Column('created_at', sa.DateTime(), server_default=sa.text("TIMEZONE('utc', CURRENT_TIMESTAMP)"), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('task_id', sa.Integer(), nullable=False),
    sa.Column('task_params', sa.JSON(), nullable=False),
    sa.Column('result', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['task_id'], ['task.id'], ),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('task_results')
