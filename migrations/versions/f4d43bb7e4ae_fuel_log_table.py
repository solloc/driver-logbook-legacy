"""Fuel Log table

Revision ID: f4d43bb7e4ae
Revises: b8cd4f22f307
Create Date: 2019-04-04 20:18:19.787535

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f4d43bb7e4ae'
down_revision = 'b8cd4f22f307'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('fuel_log',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('distance', sa.Numeric(), nullable=True),
    sa.Column('quantity', sa.Numeric(), nullable=True),
    sa.Column('recorded', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('fuel_log')
    # ### end Alembic commands ###
