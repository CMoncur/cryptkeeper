""" SmithAndCrown Excavator """

# Core Dependencies
from datetime import datetime

# External Dependencies
from bs4 import BeautifulSoup
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

# Internal Dependencies
from cryptkeeper.quarry.excavator import Excavator
import cryptkeeper.db.schema.smithandcrown as Schema
import cryptkeeper.util.util as Util


# Scraping Functions
def scrapeEnd(soup):
  """ Scrapes ICO end date from SmithAndCrown listing """
  date_string = soup \
    .findAll("td")[5] \
    .text \
    .translate({ ord(x): "" for x in [ "\n", "\r", "\t" ] }) \
    .strip()

  return datetime.strptime(date_string, "%b %d, %Y")


def scrapeName(soup):
  """ Scrapes ICO name from SmithAndCrown listing """
  return soup \
    .find("div", attrs = { "class" : "detail-col-name" }) \
    .text \
    .split("(", 1)[0] \
    .translate({ ord(x): "" for x in [ "\n", "\r", "\t" ] }) \
    .strip()


def scrapeSite(soup):
  """ Scrapes ICO site URL from SmithAndCrown listing """
  print(soup["data-url"])
  return soup["data-url"]


def scrapeStart(soup):
  """ Scrapes ICO start date from SmithAndCrown listing """
  date_string = soup \
    .findAll("td")[4] \
    .text \
    .translate({ ord(x): "" for x in [ "\n", "\r", "\t" ] }) \
    .strip()

  return datetime.strptime(date_string, "%b %d, %Y")


# Public Entities
class SmithAndCrown(Excavator):
  """ SmithAndCrown Excavator Class """

  # TODO: Place connection string in environments file
  PSQL_CONN = "postgresql+psycopg2://test:test@localhost:5432/cryptkeeper_raw"
  ENGINE = create_engine(PSQL_CONN)
  SESSION = Session(bind = ENGINE)
  URL = "https://www.smithandcrown.com/icos/"

  def __init__(self):
    super(SmithAndCrown, self).__init__([ self.URL ], True, True)
    self.raw_ico_data = []
    self.sanitized_ico_data = []

    if self.data and Util.isHtml(self.data[0]):
      soup = BeautifulSoup(self.data[0]["content"], "html.parser")

      for data in soup.findAll("tr", attrs = { "class" : "clickable-row" }):
        self.raw_ico_data.append({
          "name" : scrapeName(data),
          "start" : scrapeStart(data),
          "end" : scrapeEnd(data),
          "site" : scrapeSite(data)
        })

    else:
      print("SmithAndCrown: No data to mine...")
