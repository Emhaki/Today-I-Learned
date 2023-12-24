"""empty message

Revision ID: 8908e58a17d7
Revises: 
Create Date: 2023-12-24 14:26:07.458738

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8908e58a17d7'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('status', sa.Enum('active', 'deleted', 'blocked'), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('pw', sa.String(length=2000), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('phone_number', sa.String(length=20), nullable=True),
    sa.Column('profile_img', sa.String(length=1000), nullable=True),
    sa.Column('sns_type', sa.Enum('FB', 'G', 'K'), nullable=True),
    sa.Column('marketing_agree', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('phone_number')
    )
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
