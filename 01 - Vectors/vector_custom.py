# An Eucledean Vector Class in pure Python

# Based of Daniel Shiffman's code: https://natureofcode.com/book/chapter-1-vectors/

class PVector:

	def __init__(self, x, y, z=0):
		self.x = x
		self.y = y
		self.z = z

	def __add__(self, otherv):
		self.x += otherv.x
		self.y += otherv.y
		self.z += otherv.z
		return PVector(self.x, self.y, self.z)

