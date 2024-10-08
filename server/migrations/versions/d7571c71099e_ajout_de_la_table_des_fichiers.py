"""Ajout de la table des fichiers

Revision ID: d7571c71099e
Revises: 0851077e2a6a
Create Date: 2024-03-09 15:57:05.353154

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd7571c71099e'
down_revision = '0851077e2a6a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('username', sa.VARCHAR(length=50), nullable=False),
    sa.Column('email', sa.VARCHAR(length=120), nullable=False),
    sa.Column('first_name', sa.VARCHAR(length=50), nullable=False),
    sa.Column('last_name', sa.VARCHAR(length=50), nullable=False),
    sa.Column('password_hash', sa.VARCHAR(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###
