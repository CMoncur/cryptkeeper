""" Cryptkeeper Entry Point """

# Core Dependencies
import sys

# Internal Dependencies
from cryptkeeper.api.emailer import Emailer
from cryptkeeper.db.librarian import Librarian
import cryptkeeper.db.schema.smithandcrown as SmithAndCrownSchema
import cryptkeeper.quarry.node.icodrops as IcoDropsExcavator
import cryptkeeper.quarry.node.smithandcrown as SmithAndCrownExcavator


# Private Entities
def __getEmailBody():
  base_email_text = "New ICO listings discovered within the last 24 hours:\n\n"
  new_sc_entries = Librarian(SmithAndCrownSchema.SmithAndCrown) \
    .getLastDaysEntries()

  for entry in new_sc_entries:
    entry_text = "%s (%s): %s\n" % (entry.name, entry.token_symbol, entry.site)
    base_email_text += entry_text

  return base_email_text


# Cryptkeeper entry point
def main():
  """ Entry function """
  IcoDropsExcavator.IcoDrops()
  SmithAndCrownExcavator.SmithAndCrown()

  # The first item in the command line args list is always the path to the
  # program being run. Excluding that by grabbing the tail of the list.
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

    Otherwise, in order to start cryptkeeper without email functionality,
    simply pass no command line arguments.
  """

  if not args:
    # Don't send any e-mail, just fetch data
    pass

  elif len(args) != 5:
    print(help_text)

  else:
    conn_info = {
      "server" : args[0],
      "port" : args[1],
      "user" : args[2],
      "pw" : args[3]
    }

    emailer = Emailer(conn_info, args[4])
    emailer.sendTextEmail(__getEmailBody())


if __name__ == "__main__":
  main()
