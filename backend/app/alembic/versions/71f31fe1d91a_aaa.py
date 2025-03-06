"""aaa

Revision ID: 71f31fe1d91a
Revises: e8524821a23f
Create Date: 2025-03-06 18:12:45.917889

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel.sql.sqltypes


# revision identifiers, used by Alembic.
revision = '71f31fe1d91a'
down_revision = 'e8524821a23f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('email', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=False))
    op.add_column('user', sa.Column('hashed_password', sqlmodel.sql.sqltypes.AutoString(), nullable=False))
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_column('user', 'hashed_password')
    op.drop_column('user', 'email')
    # ### end Alembic commands ###
