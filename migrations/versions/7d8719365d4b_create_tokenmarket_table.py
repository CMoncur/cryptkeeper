# pylint: disable=E1101

"""Create Tokenmarket Table

Revision ID: 7d8719365d4b
Revises: c41ebe34a374
Create Date: 2018-03-01 13:48:13.324099

"""

# Core Dependencies
from datetime import datetime

# Other Dependencies
from alembic import op
from sqlalchemy import Column, Integer, String, TIMESTAMP


# Revision identifiers, used by Alembic.
revision = '7d8719365d4b'
down_revision = 'c41ebe34a374'
branch_labels = None
depends_on = None

# Table Name Constant
TABLE = "tokenmarket"

def upgrade():
  """Migration Up"""
  op.create_table(
    TABLE,
    Column( "id", Integer, primary_key = True, autoincrement = True ),
    Column( "created", TIMESTAMP, nullable = False, default = datetime.now ),
    Column( "name", String(100), nullable = False, unique = True ),
    Column( "start", TIMESTAMP, nullable = False ),
    Column( "end", TIMESTAMP, nullable = False ),
    Column( "site", String(200), nullable = False ),
    Column( "token_symbol", String(20), nullable = False )
  )


def downgrade():
  """Migration Down"""
  op.drop_table(TABLE)
