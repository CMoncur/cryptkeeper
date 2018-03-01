# pylint: disable=E1101

"""create icolist table

Revision ID: f831536f1e00
Revises: 7297301c6e2e
Create Date: 2018-03-01 13:24:21.294668

"""

# Core Dependencies
from datetime import datetime

# Other Dependencies
from alembic import op
from sqlalchemy import Column, Integer, String, TEXT, TIMESTAMP


# Revision identifiers, used by Alembic.
revision = 'f831536f1e00'
down_revision = '7297301c6e2e'
branch_labels = None
depends_on = None

# Table Name Constant
TABLE = ""

def upgrade():
  """Migration Up"""
  op.create_table(
    TABLE,
    Column( "id", Integer, primary_key = True, autoincrement = True ),
    Column( "created", TIMESTAMP, nullable = False, default = datetime.now ),
    Column( "name", String(100), nullable = False ),
    Column( "start", TIMESTAMP, nullable = False ),
    Column( "end", TIMESTAMP, nullable = False ),
    Column( "site", String(100), nullable = False ),
    Column( "description", TEXT, nullable = False ),
    Column( "token_symbol", String(20), nullable = False )
  )


def downgrade():
  """Migration Down"""
  op.drop_table(TABLE)
