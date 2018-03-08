""" SmithAndCrown Excavator """

# Core Dependencies
from datetime import datetime

# External Dependencies
from bs4 import BeautifulSoup
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

# Internal Dependencies
from cryptkeeper.quarry.excavator import Excavator
import cryptkeeper.db.schema.icodrops as Schema
import cryptkeeper.util.util as Util


# Public Entities
class SmithAndCrown(Excavator):
  """ SmithAndCrown Excavator Class """

  # TODO: Place connection string in environments file
  PSQL_CONN = "postgresql+psycopg2://test:test@localhost:5432/cryptkeeper_raw"
  ENGINE = create_engine(PSQL_CONN)
  SESSION = Session(bind = ENGINE)
  URL = "https://www.smithandcrown.com/icos/"

  def __init__(self):
    super(SmithAndCrown, self).__init__([ self.URL ], True, True)
