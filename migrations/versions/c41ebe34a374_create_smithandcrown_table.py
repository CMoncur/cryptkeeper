# pylint: disable=E1101

"""Create Smithandcrown Table

Revision ID: c41ebe34a374
Revises: 7215a78d17ad
Create Date: 2018-03-01 13:39:20.024536

"""

# Core Dependencies
from datetime import datetime

# Other Dependencies
from alembic import op
from sqlalchemy import Column, Integer, String, TEXT, TIMESTAMP


# Revision identifiers, used by Alembic.
revision = 'c41ebe34a374'
down_revision = '7215a78d17ad'
branch_labels = None
depends_on = None

# Table Name Constant
TABLE = "smithandcrown"

def upgrade():
  """Migration Up"""
  op.create_table(
    TABLE,
    Column( "id", Integer, primary_key = True, autoincrement = True ),
    Column( "created", TIMESTAMP, nullable = False, default = datetime.now ),
    Column( "name", String(100), nullable = False ),
    Column( "start", TIMESTAMP, nullable = False ),
    Column( "end", TIMESTAMP, nullable = False ),
    Column( "site", String(200), nullable = False ),
    Column( "description", TEXT, nullable = False ),
    Column( "report", TEXT, nullable = True ),
    Column( "raised", Integer, nullable = True ),
    Column( "token_symbol", String(20), nullable = False )
  )


def downgrade():
  """Migration Down"""
  op.drop_table(TABLE)
