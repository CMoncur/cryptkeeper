""" Entry point for proto_scrape """
# Core Dependencies
import sys

# Internal Dependencies
from proto_scrape.scrape import Scrape, ScrapeIcoDrops

help_docs = """
Error: Invalid command line argument passed.
Requires URL command line argument in the form of:
  --url VALID_URL
or
  -u VALID_URL
"""

def determineScraper(url):
  """
  Determine which scraper to use. If URL is not recognized, simply print the
  title text of whichever URL given.
  """
  if url == "https://icodrops.com/" or url == "https://icodrops.com":
    icodrops = ScrapeIcoDrops(url)
    icodrops.fetchInternalUrls()

  else:
    print("URL not recognized. I will not database the information scraped.")
    general = Scrape(url)
    general.fetchTitleText()

#Entry point
def main(args):
  """ proto_scrape entry function """
  if len(args) != 2:
    print(help_docs)

  elif (args[0] == "--url" or args[0] == "-u") and isinstance(args[1], str):
    determineScraper(args[1])

  else:
    print(help_docs)


if __name__ == "__main__":
  # Since the first argument is the script name, pass list starting from index 1
  main(sys.argv[1:])
