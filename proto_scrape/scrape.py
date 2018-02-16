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

    else:
      error_text = "Could not scrape " + url + ": " + self.status
      raise RuntimeError(error_text)

  def printData(self):
    """ Print fetched data"""
    if self.status == 200 and "text/html" in self.headers:
      print(self.data.content)

    else:
      print("Request failed: ", self.data.status_code)

  def printUrl(self):
    """ Print URL to be scraped """
    print(self.url)

  def fetchTitleText(self):
    """ Get title text from site """
    html = BeautifulSoup(self.html, "html.parser")
    for title in html.select("title"):
      print(title.text)

# class ScrapeIcoDrops(Scrape):
#   """ Scraper for IcoDrops """
#
#   def fetch
