""" Base Excavator Logic """

# Core Dependencies
import asyncio as Async
import concurrent.futures as Futures

# External Dependencies
import requests as Request
import requests.exceptions as HttpError


# Private Entities
def fetch(url):
  """ Basic HTTP request handler """
  try:
    res = Request.get(url)

    return {
      "content" : res.content,
      "error" : None,
      "status" : res.status_code,
      "type" : res.headers["Content-Type"]
    }

  except HttpError.ConnectionError as err:
    print("Connection error fetching %s: %s" % (url, err))

  except HttpError.HTTPError as err:
    print("HTTP error fetching %s: %s" % (url, err))

  except HttpError.Timeout as err:
    print("Timed out fetching %s: %s" % (url, err))

  except HttpError.TooManyRedirects as err:
    print("Too many redirects fetching %s: %s" % (url, err))


# Public Entities
class Excavator:
  """ Scrape web page from supplied URL """

  def __init__(self, urls, run_async = False, threads = 4):
    self.data = []
    self.urls = []

    for url in urls:
      if url.endswith("/"):
        self.urls.append(url[:-1])

      else:
        self.urls.append(url)

    if run_async:
      loop = Async.get_event_loop()
      loop.run_until_complete(self.__fetchParallel(threads))

    else:
      self.__fetchSeries()


  # Private Methods
  async def __fetchParallel(self, threads):
    """ Make HTTP requests for each URL in parallel (asynchronous) """
    with Futures.ThreadPoolExecutor(max_workers = threads) as ex:
      loop = Async.get_event_loop()
      data = [ loop.run_in_executor(ex, fetch, url) for url in self.urls ]

      self.data = await Async.gather(*data)


  def __fetchSeries(self):
    """ Make HTTP requests for each URL in series (synchronous) """
    for url in self.urls:
      self.data.append(fetch(url))


  # Public Methods
  def errors(self):
    """ Returns all errors within raw data list """
    errs = []

    for data in self.data:
      errs.append(data["error"])

    return errs


  def externalUrls(self):
    """ Returns supplied URL """
    return self.urls
