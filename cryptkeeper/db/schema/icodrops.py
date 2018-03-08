# pylint: disable=R0903

"""ICO Drops SqlAlchemy Schema"""

from datetime import datetime
from sqlalchemy import Column, FLOAT, Integer, String, TEXT, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class IcoDrops(Base):
  """ICO Drops Schema"""
  __tablename__ = "icodrops"

  id = Column( Integer, primary_key = True, autoincrement = True )
  created = Column( TIMESTAMP, nullable = False, default = datetime.now )
  name = Column( String(100), nullable = False )
  start = Column( TIMESTAMP, nullable = False )
  end = Column( TIMESTAMP, nullable = False )
  description = Column( TEXT, nullable = False )
  price = Column( FLOAT, nullable = False )
  raised = Column( Integer, nullable = False )
  presale_start = Column( TIMESTAMP, nullable = False )
  presale_end = Column( TIMESTAMP, nullable = False )
  token_symbol = Column( String(20), nullable = False )
