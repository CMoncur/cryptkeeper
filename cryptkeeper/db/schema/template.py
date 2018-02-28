# pylint: disable=R0903

"""Template SqlAlchemy Schema"""

from datetime import datetime
from sqlalchemy import BOOLEAN, Column, create_engine, FLOAT, Integer, \
  String, TEXT, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

# TODO: Place connection string in environments file
PSQL_CONN = "postgresql+psycopg2://test:test@localhost:5432/cryptkeeper_raw"
Base = declarative_base()
Engine = create_engine(PSQL_CONN)

class Template(Base):
  """Template Schema"""
  __tablename__ = "template"

  id = Column( Integer, primary_key = True, autoincrement = True )
  created = Column( TIMESTAMP, nullable = False, default = datetime.now )
  name = Column( String(100), nullable = False )
  start = Column( TIMESTAMP, nullable = False )
  end = Column( TIMESTAMP, nullable = False )
  site = Column( String(100), nullable = False )
  description = Column( TEXT, nullable = False )
  report = Column( TEXT, nullable = False )
  price = Column( FLOAT(20), nullable = False )
  raised = Column( BOOLEAN, nullable = False )
  presale_start = Column( TIMESTAMP, nullable = False )
  presale_end = Column( TIMESTAMP, nullable = False )
  token_symbol = Column( String(20), nullable = False )
  platform = Column( String(20), nullable = False )
