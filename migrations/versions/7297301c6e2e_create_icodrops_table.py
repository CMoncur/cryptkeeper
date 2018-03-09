# pylint: disable=E1101

"""Create Icodrops Table

Revision ID: 7297301c6e2e
Revises: b87e3608e7e3
Create Date: 2018-03-01 13:18:29.507913

"""

# Core Dependencies
from datetime import datetime

# Other Dependencies
from alembic import op
from sqlalchemy import Column, FLOAT, Integer, String, TEXT, TIMESTAMP


# Revision identifiers, used by Alembic.
revision = '7297301c6e2e'
down_revision = 'b87e3608e7e3'
branch_labels = None
depends_on = None

# Table Name Constant
TABLE = "icodrops"

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
    Column( "price", FLOAT(20), nullable = False ),
    Column( "raised", Integer, nullable = False ),
    Column( "presale_start", TIMESTAMP, nullable = False ),
    Column( "presale_end", TIMESTAMP, nullable = False ),
    Column( "token_symbol", String(20), nullable = False )
  )


def downgrade():
  """Migration Down"""
  op.drop_table(TABLE)
