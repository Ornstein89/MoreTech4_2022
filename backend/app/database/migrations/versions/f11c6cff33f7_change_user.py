"""change_user

Revision ID: f11c6cff33f7
Revises: 5963ae9c353b
Create Date: 2022-10-08 16:13:43.442813

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'f11c6cff33f7'
down_revision = '5963ae9c353b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'relevant_trends_count',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'relevant_trends_count',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###