"""Base Excavator Logic"""

from requests import get
from ..util.io import progressBar

class Excavator:
  """ Scrape web page from supplied URL """

  def __init__(self, url):
    if url.endswith("/"):
      self.url = url[:-1]

    else:
      self.url = url


  # Public Methods
  def status(self):
    """Returns status code of fetch attempt on supplied URL"""
    return self.status


  def externalUrl(self):
    """Returns supplied URL"""
    return self.url
