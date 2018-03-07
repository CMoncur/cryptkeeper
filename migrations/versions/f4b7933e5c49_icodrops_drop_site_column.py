# pylint: disable=E1101

"""icodrops drop site column

Revision ID: f4b7933e5c49
Revises: 7d8719365d4b
Create Date: 2018-03-07 13:06:55.437389

"""

from alembic import op
from sqlalchemy import Column, String


# Revision identifiers, used by Alembic.
revision = 'f4b7933e5c49'
down_revision = '7d8719365d4b'
branch_labels = None
depends_on = None

# Table Name Constant
TABLE = "icodrops"

def upgrade():
  """Migration Up"""
  op.drop_column(TABLE, "site")


def downgrade():
  """Migration Down"""
  op.add_column(
    TABLE,
    Column( "site", String(100), nullable = False )
  )
