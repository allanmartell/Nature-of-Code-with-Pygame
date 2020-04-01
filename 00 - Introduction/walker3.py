import pygame, random

class Walker:
	'''A walker that can either move forward, backward or stay put'''

	stepx = 0
	stepy = 0

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
		# because randomness happens in x,y axes
		# there are 9 choices: 2 vertical, 2 horizontal, 4 diagonal, no motion)
		
		# KEY CHANGE - Randomness
		# probabilities:
		r = random.random() # float between 0 and 1 (exclusive)

		if r < 0.4:
			#self.stepx += 1
			self.x += 1
		elif r < 0.6:
			#self.stepx -= 1
			self.x -= 1
		elif r < 0.8:
			#self.stepy += 1
			self.y += 1
		else:
			#self.stepy -= 1
			self.y -= 1

		# update position based on random step selection
		#self.x += self.stepy 
		#self.y += self.stepx

		# return to screen center if out of screen
		#if self.x < 0 or self.x > self.width:
			#self.x = self.width//2
		#if self.y < 0 or self.y > self.height:
			#self.y = self.height//2