"""Add phrase_organic model

Revision ID: c32e388a624b
Revises: 2c0404bf8969
Create Date: 2020-07-03 18:42:38.206686

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c32e388a624b'
down_revision = '2c0404bf8969'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('phraseorganic',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('database', sa.String(), nullable=True),
    sa.Column('keyword', sa.String(), nullable=False),
    sa.Column('domain', sa.String(), nullable=False),
    sa.Column('url', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_phraseorganic_database'), 'phraseorganic', ['database'], unique=False)
    op.create_index(op.f('ix_phraseorganic_domain'), 'phraseorganic', ['domain'], unique=False)
    op.create_index(op.f('ix_phraseorganic_id'), 'phraseorganic', ['id'], unique=False)
    op.create_index(op.f('ix_phraseorganic_keyword'), 'phraseorganic', ['keyword'], unique=False)
    op.create_index(op.f('ix_phraseorganic_url'), 'phraseorganic', ['url'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_phraseorganic_url'), table_name='phraseorganic')
    op.drop_index(op.f('ix_phraseorganic_keyword'), table_name='phraseorganic')
    op.drop_index(op.f('ix_phraseorganic_id'), table_name='phraseorganic')
    op.drop_index(op.f('ix_phraseorganic_domain'), table_name='phraseorganic')
    op.drop_index(op.f('ix_phraseorganic_database'), table_name='phraseorganic')
    op.drop_table('phraseorganic')
    # ### end Alembic commands ###