""" Emailer (Utility for sending emails) """

# Core Dependencies
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP, SMTPException


# Public Entities
class Emailer:
  """ Emailer Class (Utility for sending emails) """

  def __init__(self, conn_info, recipients, subject = "Cryptkeeper Update"):
    self.from_addr = "info@hoshogroup.com"
    self.recipients = recipients
    self.subject = subject

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
      msg = MIMEMultipart()
      msg["From"] = self.from_addr
      msg["To"] = self.recipients
      msg["Subject"] = self.subject
      msg.attach(MIMEText(text, "plain"))

      # Send the email
      self.SERVER.sendmail(self.from_addr, self.recipients, msg.as_string())

      print("Email sent to %s" % self.recipients)

    except SMTPException as err:
      print("Error sending email: %s" % (err))
