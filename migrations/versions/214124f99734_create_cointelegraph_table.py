# pylint: disable=E1101

"""Create Cointelegraph Table

Revision ID: 214124f99734
Revises: 28c5323d02ba
Create Date: 2018-03-01 12:00:18.084360

"""

# Core Dependencies
from datetime import datetime

# Other Dependencies
from alembic import op
from sqlalchemy import Column, Integer, String, TEXT, TIMESTAMP


# Revision identifiers, used by Alembic.
revision = '214124f99734'
down_revision = '28c5323d02ba'
branch_labels = None
depends_on = None

# Table Name Constant
TABLE = "cointelegraph"

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
    Column( "description", TEXT, nullable = False )
  )


def downgrade():
  """Migration Down"""
  op.drop_table(TABLE)
