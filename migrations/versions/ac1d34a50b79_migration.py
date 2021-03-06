"""migration.

Revision ID: ac1d34a50b79
Revises: 9fbaa12ff7ee
Create Date: 2022-05-19 13:25:23.036012

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ac1d34a50b79'
down_revision = '9fbaa12ff7ee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('feedbackcomments', sa.Column('feedback_user_id', sa.Integer(), nullable=True))
    op.drop_constraint('feedbackcomments_user_id_fkey', 'feedbackcomments', type_='foreignkey')
    op.create_foreign_key(None, 'feedbackcomments', 'users', ['feedback_user_id'], ['id'])
    op.drop_column('feedbackcomments', 'user_id')
    op.add_column('questioncomments', sa.Column('question_user_id', sa.Integer(), nullable=True))
    op.drop_constraint('questioncomments_user_id_fkey', 'questioncomments', type_='foreignkey')
    op.create_foreign_key(None, 'questioncomments', 'users', ['question_user_id'], ['id'])
    op.drop_column('questioncomments', 'user_id')
    op.add_column('shoutoutcomments', sa.Column('shoutout_user_id', sa.Integer(), nullable=True))
    op.drop_constraint('shoutoutcomments_user_id_fkey', 'shoutoutcomments', type_='foreignkey')
    op.create_foreign_key(None, 'shoutoutcomments', 'users', ['shoutout_user_id'], ['id'])
    op.drop_column('shoutoutcomments', 'user_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('shoutoutcomments', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'shoutoutcomments', type_='foreignkey')
    op.create_foreign_key('shoutoutcomments_user_id_fkey', 'shoutoutcomments', 'users', ['user_id'], ['id'])
    op.drop_column('shoutoutcomments', 'shoutout_user_id')
    op.add_column('questioncomments', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'questioncomments', type_='foreignkey')
    op.create_foreign_key('questioncomments_user_id_fkey', 'questioncomments', 'users', ['user_id'], ['id'])
    op.drop_column('questioncomments', 'question_user_id')
    op.add_column('feedbackcomments', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'feedbackcomments', type_='foreignkey')
    op.create_foreign_key('feedbackcomments_user_id_fkey', 'feedbackcomments', 'users', ['user_id'], ['id'])
    op.drop_column('feedbackcomments', 'feedback_user_id')
    # ### end Alembic commands ###
