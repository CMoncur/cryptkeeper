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

    self.__fetchIcoListUrls()


  def __fetchIcoListUrls(self):
    if Util.isHtml(self.data[0]):
      soup = BeautifulSoup(self.data[0]["content"], "html.parser")

      for s in soup.findAll("div", attrs = { "id" : "view_all" }):
        edge = s.find("a")["href"]
        self.ico_list_urls.append(self.URL + edge)
