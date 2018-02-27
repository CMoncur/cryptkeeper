# pylint: disable=R0903

"""ICO Countdown SqlAlchemy Schema"""

from datetime import datetime
from sqlalchemy import Column, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import TIMESTAMP

# TODO: Place connection string in environments file
PSQL_CONN = "postgresql+psycopg2://test:test@localhost:5432/cryptkeeper_raw"
Base = declarative_base()
Engine = create_engine(PSQL_CONN)

class IcoCountdown(Base):
  """ICO Countdown Schema"""
  __tablename__ = "icocountdown"

  id = Column( Integer, primary_key = True, autoincrement = True )
  created = Column( TIMESTAMP, nullable = False, default = datetime.now )
  # TODO: Follow up to find out what data is actually served from this source
