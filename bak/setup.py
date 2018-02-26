""" Base setup script for proto_scrape """
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
  packages = [ "cryptkeeper" ],

  # Core Dependencies
  install_requires = [
    "beautifulsoup4",
    "psycopg2",
    "sqlalchemy",
    "requests"
  ],

  # Dev/Test Dependencies
  extras_require = {
    "dev": [],
    "test": [],
  }
)
