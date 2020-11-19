"""Initial migration.

Revision ID: f97a73963d8a
Revises: 
Create Date: 2020-11-19 07:20:12.816614+00:00

"""
import sqlalchemy as sa
from alembic import op

revision = 'f97a73963d8a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('user',
    sa.Column('created_at', sa.DateTime(), server_default=sa.text("TIMEZONE('utc', CURRENT_TIMESTAMP)"),
              nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text("TIMEZONE('utc', CURRENT_TIMESTAMP)"),
              nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=False),
    sa.Column('password_hash', sa.String(length=128), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('is_superuser', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('task',
    sa.Column('created_at', sa.DateTime(), server_default=sa.text("TIMEZONE('utc', CURRENT_TIMESTAMP)"),
              nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text("TIMEZONE('utc', CURRENT_TIMESTAMP)"),
              nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('lower_limit', sa.Float(), nullable=False),
    sa.Column('upper_limit', sa.Float(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('task')
    op.drop_table('user')
