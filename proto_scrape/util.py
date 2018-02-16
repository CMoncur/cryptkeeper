""" Miscellaneous utility functions """
from sys import stdout

def progressBar(current, total, bars = 50):
  """ Render a progress bar to the console """
  filled_bars = "=" * round(current * bars / total)
  empty_bars = "-" * round((bars - len(filled_bars)))
  stdout.write("\r[%s%s] %s/%s" % (filled_bars, empty_bars, current, total))
  stdout.flush()
