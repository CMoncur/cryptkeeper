""" Cryptkeeper Entry Point """

# Core Dependencies
import sys

# Internal Dependencies
from cryptkeeper.api.emailer import Emailer
from cryptkeeper.quarry.node.icodrops import IcoDrops
from cryptkeeper.quarry.node.smithandcrown import SmithAndCrown


def __getEmailBody():
  return "this is a test :)"


# Cryptkeeper entry point
def main():
  """ Entry function """
  # IcoDrops()
  # SmithAndCrown()

  args = sys.argv[1:]
  help_text = """
    cryptkeeper expects five command line arguments in the form of:

    1) SMTP server URL
    2) SMTP server port
    3) SMTP username
    4) SMTP password
    5) Recipient email address

    Note: Emails can be sent to multiple emails by simply delimiting the
    email addresses by a comma. Example:

    example1@hello.com,example2@hello.com,example3@hello.com
  """

  if len(args) != 5:
    print(help_text)

  else:
    print(__getEmailBody())


if __name__ == "__main__":
  main()
