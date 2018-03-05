""" Miscellaneous utility functions """


def isHtml(res):
  """ Determines whether or not a response dictionary contains raw HTML """
  return res["error"] is None \
    and res["status"] == 200 \
    and "text/html" in res["type"]
