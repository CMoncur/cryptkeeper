""" Emailer (Utility for sending emails) """

# Core Dependencies
from smtplib import SMTP, SMTPException


# Public Entities
class Emailer:
  """ Emailer Class (Utility for sending emails) """

  def __init__(self, conn_info, recipients):
    self.from_addr = "info@hoshogroup.com"
    self.recipients = recipients

    try:
      self.SERVER = SMTP(conn_info["server"], conn_info["port"])
      self.SERVER.ehlo()
      self.SERVER.starttls()
      self.SERVER.ehlo()
      self.SERVER.login(conn_info["user"], conn_info["pw"])

    except SMTPException as err:
      print("Error with Emailer: %s" % (err))


  # Public Methods
  def customFromAddr(self, addr):
    """ Set custom from address for Emailer class """
    self.from_addr = addr


  def sendTextEmail(self, text):
    """ Sends text-based email """
    try:
      self.SERVER.sendmail(self.from_addr, self.recipients, text)

    except SMTPException as err:
      print("Error sending email: %s" % (err))
