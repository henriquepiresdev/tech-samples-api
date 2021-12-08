"""empty message

Revision ID: 2206dc742f10
Revises: 
Create Date: 2021-12-06 20:52:18.302036

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2206dc742f10'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users_admins',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('users_analysts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('classes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('admin_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['admin_id'], ['users_admins.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('analysis',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('batch', sa.String(), nullable=False),
    sa.Column('made', sa.DateTime(), nullable=True),
    sa.Column('category', sa.String(), nullable=False),
    sa.Column('is_concluded', sa.Boolean(), nullable=True),
    sa.Column('class_id', sa.Integer(), nullable=True),
    sa.Column('analyst_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['analyst_id'], ['users_analysts.id'], ),
    sa.ForeignKeyConstraint(['class_id'], ['classes.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('batch')
    )
    op.create_table('types',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('class_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['class_id'], ['classes.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('parameters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('unity', sa.String(), nullable=False),
    sa.Column('min', sa.String(), nullable=False),
    sa.Column('max', sa.String(), nullable=False),
    sa.Column('result', sa.String(), nullable=True),
    sa.Column('type_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['type_id'], ['types.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('parameters')
    op.drop_table('types')
    op.drop_table('analysis')
    op.drop_table('classes')
    op.drop_table('users_analysts')
    op.drop_table('users_admins')
    # ### end Alembic commands ###