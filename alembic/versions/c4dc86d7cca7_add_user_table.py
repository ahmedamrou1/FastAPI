"""add user table and created at for people table

Revision ID: c4dc86d7cca7
Revises: cb89c394ec57
Create Date: 2023-12-29 11:51:34.802209

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c4dc86d7cca7'
down_revision: Union[str, None] = 'cb89c394ec57'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("users", sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column("email", sa.String(), nullable=False),
                    sa.Column("password", sa.String(), nullable=False),
                    sa.Column("created_at", sa.String(), nullable=False),
                    sa.Column("created_at", sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
                    sa.UniqueConstraint("email"))

    op.add_column("people", sa.Column("created_at", sa.TIMESTAMP(timezone=True), server_default=sa.text('now()')), nullable=False)


def downgrade() -> None:
    op.drop_table("user")
    op.drop_column("people","created_at")
