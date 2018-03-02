"""Base Excavator Logic"""

import requests as Request
import requests.exceptions as HttpError

# Private Functions
def __fetch(url):
  """Basic HTTP request handler"""
  try:
    res = Request.get(url)
    return {
      "content" : res.data.content,
      "status" : res.data.status_code,
      "error" : None
    }

  except HttpError.ConnectionError as err:
    print("Connection error fetching %s: %s" % (url, err))

  except HttpError.HTTPError as err:
    print("HTTP error fetching %s: %s" % (url, err))

  except HttpError.Timeout as err:
    print("Timed out fetching %s: %s" % (url, err))

  except HttpError.TooManyRedirects as err:
    print("Too many redirects fetching %s: %s" % (url, err))


class Excavator:
  """ Scrape web page from supplied URL """

  def __init__(self, urls, run_async = False, threads = 20):
    self.urls = []
    self.data = []

    for url in urls:
      if url.endswith("/"):
        self.urls.append(url[:-1])

      else:
        self.urls.append(url)

    if run_async:
      self.__fetchParallel()

    else:
      self.__fetchSeries()


  # Private Methods
  def __fetchParallel(self):
    pass

  def __fetchSeries(self):
    pass


  # Public Methods
  def status(self):
    """Returns status code of fetch attempt on supplied URL"""
    return self.status


  def externalUrls(self):
    """Returns supplied URL"""
    return self.urls
