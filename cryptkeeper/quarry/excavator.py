"""Base Excavator Logic"""

import requests as Request
import requests.exceptions as HttpError

class Excavator:
  """ Scrape web page from supplied URL """

  def __init__(self, url):
    if url.endswith("/"):
      self.url = url[:-1]

    else:
      self.url = url

    try:
      self.data = Request.get(self.url)

    except HttpError.ConnectionError:
      # TODO: Handle Connection Error
      print("dang")

    except HttpError.HTTPError:
      # TODO: Handle HTTPError Error
      print("dang")

    except HttpError.Timeout:
      # TODO: Handle Timeout Error
      print("dang")

    except HttpError.TooManyRedirects:
      # TODO: Handle Connection Error
      print("dang")


  # Public Methods
  def status(self):
    """Returns status code of fetch attempt on supplied URL"""
    return self.status


  def externalUrl(self):
    """Returns supplied URL"""
    return self.url
