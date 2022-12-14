"""Add column keyword in model UrlOrganic

Revision ID: 227263f03676
Revises: 6c2e49e6702d
Create Date: 2020-07-16 18:32:01.039191

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '227263f03676'
down_revision = '6c2e49e6702d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('urlorganic', sa.Column('keyword', sa.String(), nullable=True))
    op.create_index(op.f('ix_urlorganic_keyword'), 'urlorganic', ['keyword'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_urlorganic_keyword'), table_name='urlorganic')
    op.drop_column('urlorganic', 'keyword')
    # ### end Alembic commands ###
