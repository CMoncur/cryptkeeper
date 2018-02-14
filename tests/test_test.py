# pylint: skip-file
""" General unit tests """
import unittest as UT

def addOne(i):
  return i + 1

def addMany(x, y):
  return x + y

def subOne(i):
  return i - 1

def subMany(x, y):
  return x - y

class TestAdd(UT.TestCase):
  def testAddOne(self):
    self.assertEqual(addOne(2), 3)

  def testAdd(self):
    self.assertEqual(addMany(2, 3), 5)

class TestSubtract(UT.TestCase):
  def testSubOne(self):
    self.assertEqual(subOne(2), 1)

  def testSub(self):
    self.assertEqual(subMany(5, 2), 3)
