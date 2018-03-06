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
    super(IcoDrops, self).__init__(self.__fetchIcoUrls())

    if not self.urls:
      print("IcoDrops: No URLs to mine...")

    else:
      self.__fetchIcoData()


  # Private Methods
  def __fetchIcoData(self):
    # USE THESE URLS AS SUPER FOR INIT
    print(len(self.urls))


  def __fetchIcoUrls(self):
    """
    Within IcoDrops, there are three main columns -- 1) Active ICO,
    2) Upcoming ICO, 3) Ended ICO. Each column has a "View All" anchor at
    the bottom of the list.  This function will grab the URLs for each of
    those "View All" links and append them to a list.

    Utilizing each of the gathered ICO List URLs, fetch the URLS of each
    individual ICO, and append them to a list.
    """
    icodrops_home = Excavator([ self.URL ])
    ico_list_urls = []
    ico_urls = []

    if Util.isHtml(icodrops_home.data[0]):
      soup = BeautifulSoup(icodrops_home.data[0]["content"], "html.parser")

      for s in soup.findAll("div", attrs = { "id" : "view_all" }):
        ico_list_urls.append(self.URL + s.find("a")["href"])

    ico_lists = Excavator(ico_list_urls, True)

    for data in ico_lists.data:
      if Util.isHtml(data):
        soup = BeautifulSoup(data["content"], "html.parser")

        for a in soup.findAll("a", attrs = { "id" : "ccc" }):
          ico_urls.append(a["href"])

    return ico_urls
