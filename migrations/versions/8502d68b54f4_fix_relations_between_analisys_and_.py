"""fix relations between analisys and classes

Revision ID: 8502d68b54f4
Revises: ce814e8d5128
Create Date: 2021-12-06 17:14:40.404613

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8502d68b54f4'
down_revision = 'ce814e8d5128'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('analisys', sa.Column('class_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'analisys', 'classes', ['class_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'analisys', type_='foreignkey')
    op.drop_column('analisys', 'class_id')
    # ### end Alembic commands ###
