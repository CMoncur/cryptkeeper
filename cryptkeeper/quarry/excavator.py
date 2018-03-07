""" Base Excavator Logic """

# Core Dependencies
from multiprocessing import cpu_count
import asyncio as Async
import concurrent.futures as Futures

# External Dependencies
import cfscrape as CfScrape
import requests as Request
import requests.exceptions as HttpError

# Internal Dependencies
import cryptkeeper.util.io as Io


# Private Entities
def fetch(url, cf, session):
  """
  Basic HTTP request handler

  Exceptions must be caught and handled so that cryptkeeper continues to
  mine data in the event of a bad response from a get request.
  """
  try:
    if cf:
      res = session.get(url)

    else:
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
  """
  Scrape web page from supplied URL

  Parameters:
  1) URLs: URLs to be excavated.
  2) CF: Whether or not the source URLs are protected by CloudFlare. This is
     important because Excavator will need to use CfScrape to bypass DDoS
     protection in the event that the URLs are from a CloudFlare source.
  3) Run Async: Whether or not Excavator will run asynchronously. Asynchronous
     enabled excavators run much faster than those run in series.
  4) Threads: How many worker threads the excavator will use in Asynchronous
     mode.
  """

  def __init__(self, urls, cf, run_async, threads = cpu_count()):
    self.cf = cf
    self.cf_session = CfScrape.create_scraper()
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
      data = [
        loop.run_in_executor(ex, fetch, url, self.cf, self.cf_session)
        for url in self.urls
      ]

      self.data = await Async.gather(*data)


  def __fetchSeries(self):
    """ Make HTTP requests for each URL in series (synchronous) """
    for i, url in enumerate(self.urls):
      self.data.append(fetch(url, self.cf, self.cf_session))
      Io.progressBar(i, len(self.urls), 50, "Fetching URLs...")


  # Public Methods
  def errors(self):
    """ Returns all errors within raw data list """
    errs = []

    for data in self.data:
      errs.append(data["error"])

    return list(filter(lambda x: x is not None, errs))


  def externalUrls(self):
    """ Returns supplied URL """
    return len(self.urls)
