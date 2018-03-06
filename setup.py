""" Base setup script for cryptkeeper """

from setuptools import setup

setup(
  name = "cryptkeeper",
  version = "0.0.1",
  description = "Prototype for web scraper in Python",
  url = "https://gitlab.hoshogroup.com/cmoncur/cryptkeeper",
  author = "Cody Moncur",
  author_email = "cmoncur@hoshogroup.com",
  classifiers = [
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    "Development Status :: 3 - Alpha",
    "Programming Language :: Python :: 3.6"
  ],
  packages = [
    "cryptkeeper",
    "cryptkeeper.db",
    "cryptkeeper.db.schema",
    "cryptkeeper.quarry",
    "cryptkeeper.quarry.node",
    "cryptkeeper.util"
  ],

  # Entry Point
  entry_points = {
    "console_scripts": [ "cryptkeeper = cryptkeeper.__main__:main" ]
  },

  # Core Dependencies
  install_requires = [
    "alembic",
    "beautifulsoup4",
    "cfscrape",
    "psycopg2",
    "requests",
    "sqlalchemy"
  ],

  # Dev/Test Dependencies
  extras_require = {
    "dev": [],
    "test": [],
  },

  # Scripts
  scripts = [
    "bin/migrate-down",
    "bin/migrate-up"
  ]
)
