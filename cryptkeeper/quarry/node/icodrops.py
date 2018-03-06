""" ICODrops Excavator """

# External Dependencies
from bs4 import BeautifulSoup

# Internal Dependencies
from cryptkeeper.quarry.excavator import Excavator
import cryptkeeper.util.util as Util


# Public Entities
class IcoDrops(Excavator):
  """ ICODrops Excavator Class """

  URL = "https://icodrops.com"

  def __init__(self):
    super(IcoDrops, self).__init__([ self.URL ], True)
    self.ico_list_urls = []
    self.ico_urls = []

    self.__fetchIcoUrls()


  # Private Methods
  def __fetchIcoUrls(self):
    """
    Within IcoDrops, there are three main columns -- 1) Active ICO,
    2) Upcoming ICO, 3) Ended ICO. Each column has a "View All" anchor at
    the bottom of the list.  This function will grab the URLs for each of
    those "View All" links and append them to a list.

    Utilizing each of the gathered ICO List URLs, fetch the URLS of each
    individual ICO, and append them to a list.
    """
    if Util.isHtml(self.data[0]):
      soup = BeautifulSoup(self.data[0]["content"], "html.parser")

      for s in soup.findAll("div", attrs = { "id" : "view_all" }):
        self.ico_list_urls.append(self.URL + s.find("a")["href"])

    if not self.ico_list_urls:
      print("IcoDrops: No ICO List URLs exist")

    else:
      ico_lists = Excavator(self.ico_list_urls, True)

      for data in ico_lists.data:
        if Util.isHtml(data):
          soup = BeautifulSoup(data["content"], "html.parser")

          for a in soup.findAll("a", attrs = { "id" : "ccc" }):
            self.ico_urls.append(a["href"])
