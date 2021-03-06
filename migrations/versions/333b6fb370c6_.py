"""empty message

Revision ID: 333b6fb370c6
Revises: 
Create Date: 2021-02-17 12:01:32.527068

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '333b6fb370c6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tasks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tasks')
    # ### end Alembic commands ###
