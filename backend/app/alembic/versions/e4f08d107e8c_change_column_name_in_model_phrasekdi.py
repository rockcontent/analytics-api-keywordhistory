"""Change column name in model PhraseKdi

Revision ID: e4f08d107e8c
Revises: 17f3ee828e1b
Create Date: 2020-07-07 18:31:20.096635

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e4f08d107e8c'
down_revision = '17f3ee828e1b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('phrasekdi', sa.Column('keyword_difficulty_index', sa.DECIMAL(), nullable=True))
    op.drop_column('phrasekdi', 'keyword_difficult_index')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('phrasekdi', sa.Column('keyword_difficult_index', sa.NUMERIC(), autoincrement=False, nullable=True))
    op.drop_column('phrasekdi', 'keyword_difficulty_index')
    # ### end Alembic commands ###
