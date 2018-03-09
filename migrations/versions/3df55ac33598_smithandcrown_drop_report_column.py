# pylint: disable=E1101

"""smithandcrown drop report column

Revision ID: 3df55ac33598
Revises: f4b7933e5c49
Create Date: 2018-03-08 17:05:33.246877

"""

from alembic import op
from sqlalchemy import Column, TEXT


# Revision identifiers, used by Alembic.
revision = '3df55ac33598'
down_revision = 'f4b7933e5c49'
branch_labels = None
depends_on = None

# Table Name Constant
TABLE = "smithandcrown"

def upgrade():
  """Migration Up"""
  op.drop_column(TABLE, "report")


def downgrade():
  """Migration Down"""
  op.add_column(
    TABLE,
    Column( "report", TEXT, nullable = True )
  )
