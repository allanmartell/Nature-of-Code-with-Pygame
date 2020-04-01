import pygame, random

class Walker:
	'''A walker that can either move forward, backward or stay put'''

	def __init__(self, pygamesurface):
		self.pygamesurface = pygamesurface
		self.width, self.height = self.pygamesurface.get_size()
		self.x = self.width//2
		self.y = self.height//2

	def display(self):
		color = (0,0,0)
		self.pygamesurface.lock()
		self.pygamesurface.set_at((self.x, self.y), color)
		self.pygamesurface.unlock()

	def step(self):
		# Key change: 0: stay put, 1: forward, -1: backward
		# because randomness happens in x,y axes
		# choices go from 4 to 9: 2 vertical, 2 horizontal, 4 diagonal, no motion)
		stepx = random.randint(-1, 1)
		stepy = random.randint(-1, 1)
		# update position based on random step selection
		self.x += stepy 
		self.y += stepx
