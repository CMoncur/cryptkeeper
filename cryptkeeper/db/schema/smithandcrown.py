# pylint: disable=R0903

"""Smith and Crown SqlAlchemy Schema"""

from datetime import datetime
from sqlalchemy import Column, Integer, String, TEXT, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class SmithAndCrown(Base):
  """Smith and Crown Schema"""
  __tablename__ = "smithandcrown"

  id = Column( Integer, primary_key = True, autoincrement = True )
  created = Column( TIMESTAMP, nullable = False, default = datetime.now )
  name = Column( String(100), nullable = False, unique = True )
  start = Column( TIMESTAMP, nullable = False )
  end = Column( TIMESTAMP, nullable = False )
  site = Column( String(200), nullable = False )
  description = Column( TEXT, nullable = False )
  raised = Column( Integer, nullable = True )
  token_symbol = Column( String(20), nullable = False )
