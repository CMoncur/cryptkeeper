""" Main scraper logic """
from bs4 import BeautifulSoup
from requests import get

class Scrape:
  """ Scrape web page from supplied URL """

  def __init__(self, url):
    if url.endswith("/"):
      self.url = url[:-1]

    else:
      self.url = url

    self.data = get(url)
    self.status = self.data.status_code
    self.headers = self.data.headers['Content-Type']

    if self.status == 200 and "text/html" in self.headers:
      self.html = self.data.content
      self.soup = BeautifulSoup(self.html, "html.parser")

    else:
      error_text = "Could not scrape " + url + ": " + self.status
      raise RuntimeError(error_text)

  # Public Scrape Methods
  def printData(self):
    """ Print fetched data"""
    print(self.data.content)

  def fetchTitleText(self):
    """ Get title text from site """
    print(self.soup.find("title").text)

class ScrapeIcoDrops(Scrape):
  """ Scraper for IcoDrops """

  def __init__(self, url):
    super(ScrapeIcoDrops, self).__init__(url)
    self.icoUrls = []
    self.icoAggregateUrls = []

  def fetchInternalUrls(self):
    """ Fetch URLs of ICOs to be scraped """
    for i in self.soup.findAll("div", attrs = { "id" : "view_all" }):
      edge = i.find("a")["href"]
      self.icoAggregateUrls.append(self.url + edge)

    print(self.icoAggregateUrls)
