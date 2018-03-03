""" ICODrops Excavator """

# External Dependencies
# from bs4 import BeautifulSoup

# Internal Dependencies
from quarry.excavator import Excavator


# Public Entities
class IcoDrops(Excavator):
  """ ICODrops Excavator Class """

  def __init__(self, urls):
    super(IcoDrops, self).__init__(urls, True)
