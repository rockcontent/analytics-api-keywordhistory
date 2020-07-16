"""Add column created_at on all models

Revision ID: 10245be06072
Revises: 745242717e65
Create Date: 2020-07-16 17:56:09.494243

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '10245be06072'
down_revision = '745242717e65'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('backlinksoverview', sa.Column('created_at', sa.Date(), nullable=True))
    op.add_column('domaindomains', sa.Column('created_at', sa.Date(), nullable=True))
    op.add_column('domainorganic', sa.Column('created_at', sa.Date(), nullable=True))
    op.add_column('item', sa.Column('created_at', sa.Date(), nullable=True))
    op.add_column('phraseadwords', sa.Column('created_at', sa.Date(), nullable=True))
    op.add_column('phraseadwordshistorical', sa.Column('created_at', sa.Date(), nullable=True))
    op.add_column('phraseall', sa.Column('created_at', sa.Date(), nullable=True))
    op.add_column('phrasefullsearch', sa.Column('created_at', sa.Date(), nullable=True))
    op.add_column('phrasekdi', sa.Column('created_at', sa.Date(), nullable=True))
    op.add_column('phraseorganic', sa.Column('created_at', sa.Date(), nullable=True))
    op.add_column('phraserelated', sa.Column('created_at', sa.Date(), nullable=True))
    op.add_column('phrasethis', sa.Column('created_at', sa.Date(), nullable=True))
    op.add_column('urlorganic', sa.Column('created_at', sa.Date(), nullable=True))
    op.add_column('user', sa.Column('created_at', sa.Date(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'created_at')
    op.drop_column('urlorganic', 'created_at')
    op.drop_column('phrasethis', 'created_at')
    op.drop_column('phraserelated', 'created_at')
    op.drop_column('phraseorganic', 'created_at')
    op.drop_column('phrasekdi', 'created_at')
    op.drop_column('phrasefullsearch', 'created_at')
    op.drop_column('phraseall', 'created_at')
    op.drop_column('phraseadwordshistorical', 'created_at')
    op.drop_column('phraseadwords', 'created_at')
    op.drop_column('item', 'created_at')
    op.drop_column('domainorganic', 'created_at')
    op.drop_column('domaindomains', 'created_at')
    op.drop_column('backlinksoverview', 'created_at')
    # ### end Alembic commands ###
