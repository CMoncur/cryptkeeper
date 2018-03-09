# pylint: disable=E1101

"""Create Coinschedule Table

Revision ID: 28c5323d02ba
Revises: 5834d2fd940f
Create Date: 2018-02-28 15:53:16.657869

"""

# Core Dependencies
from datetime import datetime

# Other Dependencies
from alembic import op
from sqlalchemy import Column, Integer, String, TEXT, TIMESTAMP


# Revision identifiers, used by Alembic.
revision = '28c5323d02ba'
down_revision = '5834d2fd940f'
branch_labels = None
depends_on = None

# Table Name Constant
TABLE = "coinschedule"

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
    Column( "token_symbol", String(20), nullable = False ),
    Column( "platform", String(20), nullable = False )
  )


def downgrade():
  """Migration Down"""
  op.drop_table(TABLE)
