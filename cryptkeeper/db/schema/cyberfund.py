# pylint: disable=R0903

"""Cyber Fund SqlAlchemy Schema"""

from datetime import datetime
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import TEXT, TIMESTAMP

# TODO: Place connection string in environments file
PSQL_CONN = "postgresql+psycopg2://test:test@localhost:5432/cryptkeeper_raw"
Base = declarative_base()
Engine = create_engine(PSQL_CONN)

class CyberFund(Base):
  """Cyber Fund Schema"""
  __tablename__ = "cyberfund"

  id = Column( Integer, primary_key = True, autoincrement = True )
  created = Column( TIMESTAMP, nullable = False, default = datetime.now )
  name = Column( String(100), nullable = False )
  start = Column( TIMESTAMP, nullable = False )
  end = Column( TIMESTAMP, nullable = False )
  site = Column( String(100), nullable = False )
  description = Column( TEXT, nullable = False )
  price = Column( String(20), nullable = False )
  presale_start = Column( TIMESTAMP, nullable = False )
  presale_end = Column( TIMESTAMP, nullable = False )
  token_symbol = Column( String(20), nullable = False )
