# pylint: disable=R0903

"""ICO Drops SqlAlchemy Schema"""

from datetime import datetime
from sqlalchemy import Column, create_engine, Integer, String, TEXT, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

# TODO: Place connection string in environments file
PSQL_CONN = "postgresql+psycopg2://test:test@localhost:5432/cryptkeeper_raw"
Base = declarative_base()
Engine = create_engine(PSQL_CONN)

class IcoDrops(Base):
  """ICO Drops Schema"""
  __tablename__ = "icodrops"

  id = Column( Integer, primary_key = True, autoincrement = True )
  created = Column( TIMESTAMP, nullable = False, default = datetime.now )
  name = Column( String(100), nullable = False )
  start = Column( TIMESTAMP, nullable = False )
  end = Column( TIMESTAMP, nullable = False )
  description = Column( TEXT, nullable = False )
  price = Column( String(20), nullable = False )
  raised = Column( Integer, nullable = False )
  presale_start = Column( TIMESTAMP, nullable = False )
  presale_end = Column( TIMESTAMP, nullable = False )
  token_symbol = Column( String(20), nullable = False )
