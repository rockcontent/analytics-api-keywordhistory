"""Add phrase_adword_historical model

Revision ID: 31ea8fd8b1ea
Revises: 511c9767ed95
Create Date: 2020-07-03 19:56:18.764105

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '31ea8fd8b1ea'
down_revision = '511c9767ed95'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('phraseadwordshistorical',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('database', sa.String(), nullable=True),
    sa.Column('keyword', sa.String(), nullable=False),
    sa.Column('domain', sa.String(), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('position', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('visible_url', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_phraseadwordshistorical_database'), 'phraseadwordshistorical', ['database'], unique=False)
    op.create_index(op.f('ix_phraseadwordshistorical_description'), 'phraseadwordshistorical', ['description'], unique=False)
    op.create_index(op.f('ix_phraseadwordshistorical_domain'), 'phraseadwordshistorical', ['domain'], unique=False)
    op.create_index(op.f('ix_phraseadwordshistorical_id'), 'phraseadwordshistorical', ['id'], unique=False)
    op.create_index(op.f('ix_phraseadwordshistorical_keyword'), 'phraseadwordshistorical', ['keyword'], unique=False)
    op.create_index(op.f('ix_phraseadwordshistorical_title'), 'phraseadwordshistorical', ['title'], unique=False)
    op.create_index(op.f('ix_phraseadwordshistorical_url'), 'phraseadwordshistorical', ['url'], unique=False)
    op.create_index(op.f('ix_phraseadwordshistorical_visible_url'), 'phraseadwordshistorical', ['visible_url'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_phraseadwordshistorical_visible_url'), table_name='phraseadwordshistorical')
    op.drop_index(op.f('ix_phraseadwordshistorical_url'), table_name='phraseadwordshistorical')
    op.drop_index(op.f('ix_phraseadwordshistorical_title'), table_name='phraseadwordshistorical')
    op.drop_index(op.f('ix_phraseadwordshistorical_keyword'), table_name='phraseadwordshistorical')
    op.drop_index(op.f('ix_phraseadwordshistorical_id'), table_name='phraseadwordshistorical')
    op.drop_index(op.f('ix_phraseadwordshistorical_domain'), table_name='phraseadwordshistorical')
    op.drop_index(op.f('ix_phraseadwordshistorical_description'), table_name='phraseadwordshistorical')
    op.drop_index(op.f('ix_phraseadwordshistorical_database'), table_name='phraseadwordshistorical')
    op.drop_table('phraseadwordshistorical')
    # ### end Alembic commands ###