import pygame, random
from noise import *

class Walker:
	'''A walker that can either move forward, backward or stay put'''

	stepx = 0
	stepy = 0

	def __init__(self, pygamesurface):
		self.pygamesurface = pygamesurface
		self.width, self.height = self.pygamesurface.get_size()
		#self.x = self.width//2
		#self.y = self.height//2

		self.octaves = 3 # levels of detail you want you perlin noise to have.
		self.lacunarity = 0.5 # how much detail is added or removed at each octave (adjusts frequency).

		self.tx = random.randrange(2)
		self.ty = random.randrange(1000)
		self.stepsize = random.randrange(500)

	def display(self):
		color = (0,0,0)
		self.pygamesurface.lock()
		self.pygamesurface.set_at((int(self.x), int(self.y)), color)
		self.pygamesurface.unlock()

	# emulates map in processing
	def linearConversion(self, OldValue, OldRange, NewRange):
		OldMin, OldMax = OldRange
		NewMin, NewMax = NewRange
		OldRange = (OldMax - OldMin)  
		NewRange = (NewMax - NewMin)  
		NewValue = (((OldValue - OldMin) * NewRange) / OldRange) + NewMin
		return NewValue

	def step(self):
		# because randomness happens in x,y axes
		# there are 9 choices: 2 vertical, 2 horizontal, 4 diagonal, no motion)
		
		nx = pnoise1(self.tx, octaves=self.octaves, lacunarity=self.lacunarity)
		ny = pnoise1(self.ty, octaves=self.octaves, lacunarity=self.lacunarity)
		normStep = pnoise1(self.stepsize, octaves=self.octaves, lacunarity=self.lacunarity)
		print('nx: ', nx, 'ny: ', ny)

		self.x = self.linearConversion(nx, (-1, 1), (0, self.width))
		self.y = self.linearConversion(ny, (-1, 1), (0, self.height))
		normStep = self.linearConversion(normStep, (-1, 1), (0.0, 1.5))
		print('x: ', self.x, 'y: ', self.y)

		self.tx += normStep
		self.ty += normStep