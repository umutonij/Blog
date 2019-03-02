"""Initial1238 Migration

Revision ID: d0239b2d9f05
Revises: 3181488975a8
Create Date: 2019-03-02 16:06:02.910862

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd0239b2d9f05'
down_revision = '3181488975a8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('delete')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('delete',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('comment', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('blog_title', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('blog_content', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='delete_pkey')
    )
    # ### end Alembic commands ###
