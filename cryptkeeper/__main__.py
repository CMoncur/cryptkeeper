""" Cryptkeeper Entry Point """

# Core Dependencies
# import sys

# Internal Dependencies
from cryptkeeper.quarry.node.icodrops import IcoDrops

def main():
  """ Entry function """
  hello = IcoDrops()
  print(hello.ico_list_urls)

if __name__ == "__main__":
  main()
