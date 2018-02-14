""" Main scraper logic """
from bs4 import BeautifulSoup
from requests import get
from requests.exceptions import RequestException

class Scrape:
  """ Scrape web page from supplied URL """

  def __init__(self, url):
    """ Fetch URL """
    self.url = url
    print("hi")

  def printUrl(self):
    """ Print URL to be scraped """
    print(self.url)

  # def __responseStatus(self, ):
  #   """ Check if response is good """
