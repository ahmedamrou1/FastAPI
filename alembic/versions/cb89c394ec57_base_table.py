"""base table

Revision ID: cb89c394ec57
Revises: 
Create Date: 2023-12-29 11:46:27.849555

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cb89c394ec57'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("people", sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column("first_name", sa.String(), nullable=False),
                    sa.Column("last_name", sa.String(), nullable=False),
                    sa.Column("gender", sa.String(), nullable=False),
                    sa.Column("email", sa.String(), nullable=False),
                    sa.Column("phone", sa.String(), nullable=False))
    pass
    

def downgrade() -> None:
    op.drop_table("people")
    pass
