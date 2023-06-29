"""empty message

Revision ID: e0bade2236f6
Revises: 
Create Date: 2023-06-29 13:00:55.310857

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e0bade2236f6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('clients',
    sa.Column('idClient', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('fone', sa.String(length=11), nullable=False),
    sa.Column('maritalStatus', sa.String(length=30), nullable=False),
    sa.Column('address', sa.String(length=60), nullable=False),
    sa.PrimaryKeyConstraint('idClient')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('clients')
    # ### end Alembic commands ###
