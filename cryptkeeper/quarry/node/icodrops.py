""" ICODrops Excavator """

# External Dependencies
from bs4 import BeautifulSoup

# Internal Dependencies
from cryptkeeper.quarry.excavator import Excavator
import cryptkeeper.util.util as Util


# Scraping Functions
def scrapeDescription(soup):
  """ Scrapes ICO description from ICODrops listing """
  return soup \
    .find("div", attrs = { "class" : "ico-main-info" }) \
    .text \
    .replace("\n", " ") \
    .translate({ ord(x): "" for x in ["\r", "\t" ] }) \
    .strip()


def scrapeName(soup):
  """ Scrapes ICO name from ICODrops listing """
  return soup \
    .find("div", attrs = { "class" : "ico-main-info" }) \
    .find("h3").text


def scrapePrice(soup):
  """ Scrapes ICO proce from ICODrops listing """
  li = soup.findAll("li")


  for idx, yeah in enumerate(li):
    span = yeah.find("span", attrs = { "class" : "grey" })

    if span and "Token Price" in span.text:
      # Return only first match
      return li[idx].text \
        .split(" = ")[-1] \
        .split(" (")[0] \
        .replace("\xa0", " ") # Replace space character code with a space...

  # Catchall in the event no matches are found
  return None


def scrapeRaised(soup):
  """ Scrapes ICO amount raised from ICODrops listing """
  return soup \
    .find("div", attrs = { "class" : "money-goal" }) \
    .text \
    .translate({ ord(x): "" for x in [ "\n", "\r", "\t" ] })


def scrapeSite(soup):
  """ Scrapes ICO website URL from ICODrops listing """
  return soup \
    .find("div", attrs = { "class" : "ico-right-col" }) \
    .find("a")["href"]


def scrapeStartEnd(soup):
  """ Scrapes ICO start date from ICODrops listing """
  token_sale = list(filter(lambda x: "Sale:" in x.text, soup.findAll("h4")))
  return token_sale[0] \
    .text \
    .translate({ ord(x): "" for x in [ "\n", "\r", "\t" ] }) \
    .replace("Token Sale: ", "")


# Public Entities
class IcoDrops(Excavator):
  """ ICODrops Excavator Class """

  URL = "https://icodrops.com"

  def __init__(self):
    # TODO: Uncomment when ready for real deal
    # super(IcoDrops, self).__init__(self.__fetchIcoUrls(), True, True)
    yeah = self.__fetchIcoUrls()
    super(IcoDrops, self).__init__([ yeah[0], yeah[1], yeah[2] ], True, True)
    self.raw_ico_data = []

    if not self.urls:
      print("IcoDrops: No URLs to mine...")

    else:
      self.__fetchIcoData()


  # Private Methods
  def __fetchIcoData(self):
    """ Fetch metadata specific to each ICO """
    # Filter out non-HTML responses
    self.data = list(filter(Util.isHtml, self.data))

    for data in self.data:
      soup = BeautifulSoup(data["content"], "html.parser")

      self.raw_ico_data.append({
        "name" : scrapeName(soup),
        "start" : scrapeStartEnd(soup),
        "end" : scrapeStartEnd(soup),
        # "site" : scrapeSite(soup), # TODO: Migration to remove this field
        "description" : scrapeDescription(soup),
        "price" : scrapePrice(soup),
        "raised" : scrapeRaised(soup),
      })


  def __fetchIcoUrls(self):
    """
    Within IcoDrops, there are three main columns -- 1) Active ICO,
    2) Upcoming ICO, 3) Ended ICO. Each column has a "View All" anchor at
    the bottom of the list.  This function will grab the URLs for each of
    those "View All" links and append them to a list.

    Utilizing each of the gathered ICO List URLs, fetch the URLS of each
    individual ICO, and append them to a list.
    """
    icodrops_home = Excavator([ self.URL ], True, True)
    ico_list_urls = []
    ico_urls = []

    if Util.isHtml(icodrops_home.data[0]):
      soup = BeautifulSoup(icodrops_home.data[0]["content"], "html.parser")

      for s in soup.findAll("div", attrs = { "id" : "view_all" }):
        ico_list_urls.append(self.URL + s.find("a")["href"])

    ico_lists = Excavator(ico_list_urls, True, True)

    for data in ico_lists.data:
      if Util.isHtml(data):
        soup = BeautifulSoup(data["content"], "html.parser")

        for a in soup.findAll("a", attrs = { "id" : "ccc" }):
          ico_urls.append(a["href"])

    return ico_urls
