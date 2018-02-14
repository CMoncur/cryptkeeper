""" Base setup script for proto_scrape """
from setuptools import setup

setup(
  name = "proto_scrape",
  version = "0.0.1",
  description = "Prototype for web scraper in Python",
  url = "https://gitlab.hoshogroup.com/cmoncur/proto_scrape",
  author = "Cody Moncur",
  author_email = "cmoncur@hoshogroup.com",
  classifiers = [
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    "Development Status :: 3 - Alpha",
    "Programming Language :: Python :: 3.6"
  ],
  packages = [ "src" ],

  # Core Dependencies
  install_requires = [
    "beautifulsoup4",
    "requests"
  ],

  # Dev/Test Dependencies
  extras_require = {
    "dev": [],
    "test": [],
  }
)
