import math

# get string from input and output string.upper()
class String(object):
	def init__(self):
		self._string = ""

	def getString(self):
		self._string = raw_input("Please enter string: ")

	def printString(self):
		print self._string.upper()

# static method
class American(object):
	@staticmethod
	def printNationality():
		print "American"

# compute area of circle and rectangle
class Circle(object):
	def __init__(self, radius):
		self._r = radius

	def area(self):
		return math.pi * self._r**2

class Rectangle(object):
	def __init__(self, length, width):
		self._l = length
		self._w = width

	def area(self):
		return self._l * self._w