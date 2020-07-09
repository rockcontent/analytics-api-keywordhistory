"""Add column token to User model

Revision ID: d91bb8ef389c
Revises: 44f825d5b725
Create Date: 2020-07-09 13:02:46.884279

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd91bb8ef389c'
down_revision = '44f825d5b725'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('item_owner_id_fkey', 'item', type_='foreignkey')
    op.drop_column('item', 'owner_id')
    op.add_column('user', sa.Column('token', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'token')
    op.add_column('item', sa.Column('owner_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('item_owner_id_fkey', 'item', 'user', ['owner_id'], ['id'])
    # ### end Alembic commands ###