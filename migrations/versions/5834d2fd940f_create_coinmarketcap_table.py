# pylint: disable=E1101

"""Create Coinmarketcap Table

Revision ID: 5834d2fd940f
Revises: f3b14bc33281
Create Date: 2018-02-28 15:48:43.014789

"""

# Core Dependencies
from datetime import datetime

# Other Dependencies
from alembic import op
from sqlalchemy import Column, Integer, TIMESTAMP


# Revision identifiers, used by Alembic.
revision = '5834d2fd940f'
down_revision = 'f3b14bc33281'
branch_labels = None
depends_on = None

# Table Name Constant
TABLE = "coinmarketcap"

def upgrade():
  """Migration Up"""
  op.create_table(
    TABLE,
    Column( "id", Integer, primary_key = True, autoincrement = True ),
    Column( "created", TIMESTAMP, nullable = False, default = datetime.now )
  )


def downgrade():
  """Migration Down"""
  op.drop_table(TABLE)
