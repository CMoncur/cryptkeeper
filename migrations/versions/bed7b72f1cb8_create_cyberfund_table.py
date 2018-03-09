# pylint: disable=E1101

"""Create Cyberfund Table

Revision ID: bed7b72f1cb8
Revises: 214124f99734
Create Date: 2018-03-01 12:15:49.623039

"""

# Core Dependencies
from datetime import datetime

# Other Dependencies
from alembic import op
from sqlalchemy import Column, FLOAT, Integer, String, TEXT, TIMESTAMP


# Revision identifiers, used by Alembic.
revision = 'bed7b72f1cb8'
down_revision = '214124f99734'
branch_labels = None
depends_on = None

# Table Name Constant
TABLE = "cyberfund"

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
    Column( "description", TEXT, nullable = False ),
    Column( "price", FLOAT(20), nullable = False ),
    Column( "presale_start", TIMESTAMP, nullable = False ),
    Column( "presale_end", TIMESTAMP, nullable = False ),
    Column( "token_symbol", String(20), nullable = False )
  )


def downgrade():
  """Migration Down"""
  op.drop_table(TABLE)
