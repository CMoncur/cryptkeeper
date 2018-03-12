""" Cryptkeeper Entry Point """

# Core Dependencies
# import sys

# Internal Dependencies
from cryptkeeper.quarry.node.icodrops import IcoDrops
from cryptkeeper.quarry.node.smithandcrown import SmithAndCrown

def main():
  """ Entry function """
  IcoDrops()
  SmithAndCrown()

if __name__ == "__main__":
  main()
