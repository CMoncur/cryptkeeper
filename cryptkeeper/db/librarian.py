""" Librarian (Databasing Utility for Miners) """

# External Dependencies
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session


# Public Entities
class Librarian:
  """ Librarian Class (Databasing Utilities for Miners) """

  # TODO: Place connection string in environments file
  PSQL_CONN = "postgresql+psycopg2://test:test@localhost:5432/cryptkeeper_raw"

  def __init__(self, schema):
    self.ENGINE = create_engine(self.PSQL_CONN)
    self.SESSION = Session(bind = self.ENGINE)
    self.SCHEMA = schema


  def bulkInsert(self, items):
    """
    Inserts a list of items into the table of supplied schema, implementing
    `bulk_insert_mappings`. Unlike other methods, `bulkInsert` akes a list
    of dictionaries and performs the mapping to the schema as opposed to
    taking items that have already been mapped according to the schema
    thereunto pertaining.
    """
    try:
      self.SESSION.bulk_insert_mappings(
        self.SCHEMA, items
      )
      self.SESSION.commit()

    except SQLAlchemyError as err:
      print("SmithAndCrown: Error storing daata: %s" % (err))


  def bulkUpsert(self):
    """
    Either inserts or updates items into the table of supplied schema.
    Requires items to be mapped prior to being passed to this method.
    """
    print(self.PSQL_CONN)
