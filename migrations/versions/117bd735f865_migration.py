"""migration.

Revision ID: 117bd735f865
Revises: 67b3cb94d467
Create Date: 2022-05-19 02:33:09.615791

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '117bd735f865'
down_revision = '67b3cb94d467'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('questions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category', sa.String(length=200), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('shoutouts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category', sa.String(length=200), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('comments', sa.Column('feedback_id', sa.Integer(), nullable=True))
    op.drop_constraint('comments_pitch_id_fkey', 'comments', type_='foreignkey')
    op.create_foreign_key(None, 'comments', 'feedback', ['feedback_id'], ['id'])
    op.drop_column('comments', 'pitch_id')
    op.add_column('downvotes', sa.Column('feedback_id', sa.Integer(), nullable=True))
    op.drop_constraint('downvotes_pitch_id_fkey', 'downvotes', type_='foreignkey')
    op.create_foreign_key(None, 'downvotes', 'feedback', ['feedback_id'], ['id'])
    op.drop_column('downvotes', 'pitch_id')
    op.add_column('upvotes', sa.Column('feedback_id', sa.Integer(), nullable=True))
    op.drop_constraint('upvotes_pitch_id_fkey', 'upvotes', type_='foreignkey')
    op.create_foreign_key(None, 'upvotes', 'feedback', ['feedback_id'], ['id'])
    op.drop_column('upvotes', 'pitch_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('upvotes', sa.Column('pitch_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'upvotes', type_='foreignkey')
    op.create_foreign_key('upvotes_pitch_id_fkey', 'upvotes', 'feedback', ['pitch_id'], ['id'])
    op.drop_column('upvotes', 'feedback_id')
    op.add_column('downvotes', sa.Column('pitch_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'downvotes', type_='foreignkey')
    op.create_foreign_key('downvotes_pitch_id_fkey', 'downvotes', 'feedback', ['pitch_id'], ['id'])
    op.drop_column('downvotes', 'feedback_id')
    op.add_column('comments', sa.Column('pitch_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.create_foreign_key('comments_pitch_id_fkey', 'comments', 'feedback', ['pitch_id'], ['id'])
    op.drop_column('comments', 'feedback_id')
    op.drop_table('shoutouts')
    op.drop_table('questions')
    # ### end Alembic commands ###
