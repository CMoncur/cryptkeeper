""" Librarian (Databasing Utility for Miners) """

# External Dependencies
from sqlalchemy import create_engine
from sqlalchemy.dialects import postgresql
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


  # Public Methods
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
      print("Error with bulk insert: %s" % (err))


  def bulkInsertDoNothingOnConflict(self, items, unique_fields):
    """
    Either inserts items into the table of supplied schema or does nothing.
    Requires items to be mapped prior to being passed to this method.
    """
    try:
      statement = postgresql \
        .insert(self.SCHEMA.__table__) \
        .values(items) \
        .on_conflict_do_nothing(index_elements = unique_fields)

      self.SESSION.execute(statement)
      self.SESSION.commit()

    except SQLAlchemyError as err:
      print("Error with bulk insert: %s" % (err))


  def bulkUpsert(self, items, unique_fields):
    """
    Either inserts items into the table of supplied schema or updates
    conflicting field. Requires items to be mapped prior to being passed to
    this method.
    """
    try:
      for item in items:
        statement = postgresql \
          .insert(self.SCHEMA.__table__) \
          .values(item) \
          .on_conflict_do_update(
            index_elements = unique_fields,
            set_ = item
          )

        self.SESSION.execute(statement)

      self.SESSION.commit()

    except SQLAlchemyError as err:
      print("Error with bulk upsert: %s" % (err))
