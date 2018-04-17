"""empty message

Revision ID: e3ff1eb5c5fe
Revises: 
Create Date: 2018-04-17 21:12:39.334732

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e3ff1eb5c5fe'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('collects',
    sa.Column('collecter_id', sa.Integer(), nullable=False),
    sa.Column('collected_id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['collected_id'], ['novels.id'], ),
    sa.ForeignKeyConstraint(['collecter_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('collecter_id', 'collected_id')
    )
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('disabled', sa.Boolean(), nullable=True),
    sa.Column('audienc_id', sa.Integer(), nullable=True),
    sa.Column('novel_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['audienc_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['novel_id'], ['novels.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_comments_timestamp'), 'comments', ['timestamp'], unique=False)
    op.create_index(op.f('ix_novels_update_time'), 'novels', ['update_time'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_novels_update_time'), table_name='novels')
    op.drop_index(op.f('ix_comments_timestamp'), table_name='comments')
    op.drop_table('comments')
    op.drop_table('collects')
    # ### end Alembic commands ###
