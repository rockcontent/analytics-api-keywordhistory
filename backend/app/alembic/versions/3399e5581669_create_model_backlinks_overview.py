"""Create model backlinks overview

Revision ID: 3399e5581669
Revises: 85d8813af81f
Create Date: 2020-07-15 12:51:36.349073

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3399e5581669'
down_revision = '85d8813af81f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('backlinksoverview',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('domain', sa.String(), nullable=False),
    sa.Column('total', sa.Integer(), nullable=False),
    sa.Column('domains_num', sa.Integer(), nullable=False),
    sa.Column('ips_num', sa.Integer(), nullable=False),
    sa.Column('follows_num', sa.Integer(), nullable=False),
    sa.Column('nofollows_num', sa.Integer(), nullable=False),
    sa.Column('score', sa.Integer(), nullable=False),
    sa.Column('trust_score', sa.Integer(), nullable=False),
    sa.Column('urls_num', sa.Integer(), nullable=False),
    sa.Column('ipclassc_num', sa.Integer(), nullable=False),
    sa.Column('texts_num', sa.Integer(), nullable=False),
    sa.Column('forms_num', sa.Integer(), nullable=False),
    sa.Column('frames_num', sa.Integer(), nullable=False),
    sa.Column('images_num', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_backlinksoverview_domain'), 'backlinksoverview', ['domain'], unique=False)
    op.create_index(op.f('ix_backlinksoverview_id'), 'backlinksoverview', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_backlinksoverview_id'), table_name='backlinksoverview')
    op.drop_index(op.f('ix_backlinksoverview_domain'), table_name='backlinksoverview')
    op.drop_table('backlinksoverview')
    # ### end Alembic commands ###