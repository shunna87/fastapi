"""empty message

Revision ID: 7442c0a30337
Revises: 827e2ae8fd9a
Create Date: 2022-05-25 15:39:09.353821

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7442c0a30337'
down_revision = '827e2ae8fd9a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'votes', 'posts', ['post_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'votes', 'users', ['user_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'votes', type_='foreignkey')
    op.drop_constraint(None, 'votes', type_='foreignkey')
    # ### end Alembic commands ###
