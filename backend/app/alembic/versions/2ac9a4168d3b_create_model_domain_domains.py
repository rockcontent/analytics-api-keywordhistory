"""Create model domain domains

Revision ID: 2ac9a4168d3b
Revises: 93975216e147
Create Date: 2020-07-14 20:40:41.908638

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2ac9a4168d3b'
down_revision = '93975216e147'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('domaindomains',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('database', sa.String(), nullable=True),
    sa.Column('keyword', sa.String(), nullable=False),
    sa.Column('domains_query', sa.String(), nullable=False),
    sa.Column('domain', sa.String(), nullable=False),
    sa.Column('search_volume', sa.Integer(), nullable=False),
    sa.Column('cpc', sa.DECIMAL(), nullable=False),
    sa.Column('competition', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_domaindomains_database'), 'domaindomains', ['database'], unique=False)
    op.create_index(op.f('ix_domaindomains_domain'), 'domaindomains', ['domain'], unique=False)
    op.create_index(op.f('ix_domaindomains_domains_query'), 'domaindomains', ['domains_query'], unique=False)
    op.create_index(op.f('ix_domaindomains_id'), 'domaindomains', ['id'], unique=False)
    op.create_index(op.f('ix_domaindomains_keyword'), 'domaindomains', ['keyword'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_domaindomains_keyword'), table_name='domaindomains')
    op.drop_index(op.f('ix_domaindomains_id'), table_name='domaindomains')
    op.drop_index(op.f('ix_domaindomains_domains_query'), table_name='domaindomains')
    op.drop_index(op.f('ix_domaindomains_domain'), table_name='domaindomains')
    op.drop_index(op.f('ix_domaindomains_database'), table_name='domaindomains')
    op.drop_table('domaindomains')
    # ### end Alembic commands ###
