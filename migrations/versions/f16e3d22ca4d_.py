"""empty message

Revision ID: f16e3d22ca4d
Revises: 7d66f834bc9e
Create Date: 2020-11-17 21:51:49.674557

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f16e3d22ca4d'
down_revision = '7d66f834bc9e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('can_review_tasks', sa.Boolean(), nullable=False, default=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'can_review_tasks')
    # ### end Alembic commands ###
