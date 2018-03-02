""" Cryptkeeper Entry Point """

# Core Dependencies
import sys

# Internal Dependencies
from quarry.node.icodrops import IcoDrops

def main():
  """ Entry function """
  urls = [ sys.argv[1] ] * 1000
  hello = IcoDrops(urls)
  print(hello.errors())

if __name__ == "__main__":
  main()
