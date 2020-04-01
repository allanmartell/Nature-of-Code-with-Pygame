import pygame, random

class Walker:

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
		choice = random.randint(0, 4)
		if choice == 0:
			self.x += 1
		elif choice == 1:
			self.x -= 1
		elif choice == 2:
			self.y += 1
		elif choice == 3:
			self.y -= 1

