# pylint: disable=E1101

"""Create Template Table

Revision ID: f3b14bc33281
Revises:
Create Date: 2018-02-28 14:42:01.583542

"""

# Core Dependencies
from datetime import datetime

# Other Dependencies
from alembic import op
from sqlalchemy import Column, FLOAT, Integer, String, TEXT, TIMESTAMP


# Revision identifiers, used by Alembic.
revision = 'f3b14bc33281'
down_revision = None
branch_labels = None
depends_on = None

# Table Name Constant
TABLE = "template"

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
    Column( "report", TEXT, nullable = False ),
    Column( "price", FLOAT, nullable = False ),
    Column( "raised", Integer, nullable = False ),
    Column( "presale_start", TIMESTAMP, nullable = False ),
    Column( "presale_end", TIMESTAMP, nullable = False ),
    Column( "token_symbol", String(20), nullable = False ),
    Column( "platform", String(20), nullable = False )
  )


def downgrade():
  """Migration Down"""
  op.drop_table(TABLE)
