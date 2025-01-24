"""added cartitem relationship to user

Revision ID: 520c5c31f03c
Revises: b22148097910
Create Date: 2025-01-24 11:43:20.659371

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '520c5c31f03c'
down_revision = 'b22148097910'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order_item')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('order_item',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('order_id', sa.INTEGER(), nullable=False),
    sa.Column('product_id', sa.INTEGER(), nullable=False),
    sa.Column('product_name', sa.VARCHAR(length=100), nullable=False),
    sa.Column('price', sa.FLOAT(), nullable=False),
    sa.Column('quantity', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['order_id'], ['order.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
