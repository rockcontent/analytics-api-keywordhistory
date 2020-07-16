"""Change type of column serp_features in model UrlOrganic

Revision ID: 583eccbb7227
Revises: fd37026d59fc
Create Date: 2020-07-16 18:43:37.667121

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '583eccbb7227'
down_revision = 'fd37026d59fc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('urlorganic', 'serp_features',
               existing_type=sa.INTEGER(),
               type_=sa.String(),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('urlorganic', 'serp_features',
               existing_type=sa.String(),
               type_=sa.INTEGER(),
               existing_nullable=False)
    # ### end Alembic commands ###
