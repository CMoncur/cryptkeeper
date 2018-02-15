""" Main scraper logic """
# from bs4 import BeautifulSoup
from requests import get
# from requests.exceptions import RequestException

class Scrape:
  """ Scrape web page from supplied URL """

  def __init__(self, url):
    """ Fetch URL """
    self.url = url
    self.data = get(url)

  def printData(self):
    """ Print fetched data"""
    if self.data.status_code == 200:
      print(self.data.content)

    else:
      print("Request failed: ", self.data.status_code)

  def printUrl(self):
    """ Print URL to be scraped """
    print(self.url)

  # def __responseStatus(self, ):
  #   """ Check if response is good """
