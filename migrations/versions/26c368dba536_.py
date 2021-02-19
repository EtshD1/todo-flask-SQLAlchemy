"""empty message

Revision ID: 26c368dba536
Revises: 1696db2e3765
Create Date: 2021-02-18 12:58:29.381394

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '26c368dba536'
down_revision = '1696db2e3765'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('list',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('tasks', sa.Column('list_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'tasks', 'list', ['list_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'tasks', type_='foreignkey')
    op.drop_column('tasks', 'list_id')
    op.drop_table('list')
    # ### end Alembic commands ###
