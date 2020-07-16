"""Add field target on model BacklinksOverview

Revision ID: cf43dca964ed
Revises: 3399e5581669
Create Date: 2020-07-15 13:23:11.766520

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cf43dca964ed'
down_revision = '3399e5581669'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('backlinksoverview', sa.Column('target', sa.String(), nullable=False))
    op.create_index(op.f('ix_backlinksoverview_target'), 'backlinksoverview', ['target'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_backlinksoverview_target'), table_name='backlinksoverview')
    op.drop_column('backlinksoverview', 'target')
    # ### end Alembic commands ###