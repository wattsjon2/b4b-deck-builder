"""changed card table

Revision ID: 17be9403802d
Revises: ff1c6b7832a5
Create Date: 2021-12-10 10:44:50.009276

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '17be9403802d'
down_revision = 'ff1c6b7832a5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('card',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('card_name', sa.String(length=150), nullable=True),
    sa.Column('card_description', sa.String(length=250), nullable=True),
    sa.Column('supply_line', sa.String(length=100), nullable=True),
    sa.Column('supply_track', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('card')
    # ### end Alembic commands ###