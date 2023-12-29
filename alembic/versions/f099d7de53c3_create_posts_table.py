"""create posts table

Revision ID: f099d7de53c3
Revises: 
Create Date: 2023-12-28 20:37:15.133792

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f099d7de53c3'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("People", sa.Column("id", sa.Integer(), nullable=False, primary_key=True), sa.Column("first_name", sa.String(), mullable=False))
    pass


def downgrade() -> None:
    op.drop_table("People")
    pass
