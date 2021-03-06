"""add year to song table

Revision ID: b06a819d059d
Revises: a95cdc9b32a3
Create Date: 2021-10-05 19:25:23.273342

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = 'b06a819d059d'
down_revision = 'a95cdc9b32a3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('song', sa.Column('year', sa.Integer(), nullable=True))
    # op.alter_column('song', 'id',
    #            existing_type=sa.INTEGER(),
    #            nullable=True,
    #            autoincrement=True)
    op.create_index(op.f('ix_song_year'), 'song', ['year'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_song_year'), table_name='song')
    # op.alter_column('song', 'id',
    #            existing_type=sa.INTEGER(),
    #            nullable=False,
    #            autoincrement=True)
    op.drop_column('song', 'year')
    # ### end Alembic commands ###
