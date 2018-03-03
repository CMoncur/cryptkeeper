""" Base setup script for cryptkeeper """

from setuptools import find_packages, setup

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
  packages = find_packages(),

  # Entry Point
  entry_points = {
    "console_scripts": [ "cryptkeeper = cryptkeeper.__main__:main" ]
  },

  # Core Dependencies
  install_requires = [
    "alembic",
    "beautifulsoup4",
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
