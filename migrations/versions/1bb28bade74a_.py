"""empty message

Revision ID: 1bb28bade74a
Revises: 1b18ed523f10
Create Date: 2018-03-17 02:10:51.639503

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1bb28bade74a'
down_revision = '1b18ed523f10'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profile', sa.Column('location', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_profile', 'location')
    # ### end Alembic commands ###
