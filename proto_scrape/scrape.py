""" Main scraper logic """
from bs4 import BeautifulSoup
from requests import get

class Scrape:
  """ Scrape web page from supplied URL """

  def __init__(self, url):
    """ Fetch URL """
    self.url = url
    self.data = get(url)
    self.status = self.data.status_code
    self.headers = self.data.headers['Content-Type']
    if self.status == 200 and "text/html" in self.headers:
      self.html = self.data.content

  def printData(self):
    """ Print fetched data"""
    if self.status == 200 and "text/html" in self.headers:
      print(self.data.content)

    else:
      print("Request failed: ", self.data.status_code)

  def printUrl(self):
    """ Print URL to be scraped """
    print(self.url)

  def getHeaderText(self):
    """ Get h1 text from site """
    html = BeautifulSoup(self.html, 'html.parser')
    for h1 in html.select('h1'):
      print(h1.text)
