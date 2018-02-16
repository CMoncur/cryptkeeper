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

    # TODO: Make a proper URL fetch utility
    self.data = get(url)
    self.status = self.data.status_code
    self.headers = self.data.headers['Content-Type']

    if self.status == 200 and "text/html" in self.headers:
      self.html = self.data.content
      self.soup = BeautifulSoup(self.html, "html.parser")

    else:
      # TODO: Normalize the way errors are thrown
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
    self.ico_urls = []
    self.ico_aggregate_urls = []

  # Private ScrapeIcoDrops Methods
  def __fetchInternalUrls(self):
    """ Fetch URLs of ICOs to be scraped """
    for i in self.soup.findAll("div", attrs = { "id" : "view_all" }):
      edge = i.find("a")["href"]
      self.ico_aggregate_urls.append(self.url + edge)

    for url in self.ico_aggregate_urls:
      # TODO: Make a proper URL fetch utility
      data = get(url)
      if data.status_code == 200 and "html" in data.headers['Content-Type']:
        soup = BeautifulSoup(data.content, "html.parser")
        for a in soup.findAll("a", attrs = { "id" : "ccc" }):
          self.ico_urls.append(a["href"])

      else:
        # TODO: Normalize the way errors are thrown
        error_text = "Could not scrape " + url + ": " + self.status
        raise RuntimeError(error_text)


  # Public ScrapeIcoDrops Methods
  def fetchData(self):
    """ Fetch data from IcoDrops """
    self.__fetchInternalUrls()
    print(self.ico_urls)
