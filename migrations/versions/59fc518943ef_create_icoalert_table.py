# pylint: disable=E1101

"""Create Icoalert Table

Revision ID: 59fc518943ef
Revises: bed7b72f1cb8
Create Date: 2018-03-01 12:54:39.505991

"""

# Core Dependencies
from datetime import datetime

# Other Dependencies
from alembic import op
from sqlalchemy import Column, Integer, String, TEXT, TIMESTAMP


# Revision identifiers, used by Alembic.
revision = '59fc518943ef'
down_revision = 'bed7b72f1cb8'
branch_labels = None
depends_on = None

# Table Name Constant
TABLE = "icoalert"

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
    Column( "presale_start", TIMESTAMP, nullable = False ),
    Column( "presale_end", TIMESTAMP, nullable = False )
  )


def downgrade():
  """Migration Down"""
  op.drop_table(TABLE)
