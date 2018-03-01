# pylint: disable=E1101

"""Create Icorating Table

Revision ID: 7215a78d17ad
Revises: f831536f1e00
Create Date: 2018-03-01 13:36:18.543323

"""

# Core Dependencies
from datetime import datetime

# Other Dependencies
from alembic import op
from sqlalchemy import Column, Integer, TIMESTAMP


# Revision identifiers, used by Alembic.
revision = '7215a78d17ad'
down_revision = 'f831536f1e00'
branch_labels = None
depends_on = None

# Table Name Constant
TABLE = "icorating"

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
