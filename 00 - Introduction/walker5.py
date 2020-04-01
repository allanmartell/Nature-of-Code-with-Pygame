import pygame, random, math

class Walker:
	'''A walker that can either move forward, backward or stay put'''

	stepx = 0
	stepy = 0

	def __init__(self, pygamesurface):
		self.pygamesurface = pygamesurface
		self.width, self.height = self.pygamesurface.get_size()
		#self.mouseX, self.mouseY = pygame.mouse.get_pos()
		self.x = self.width//2
		self.y = self.height//2

	def display(self):
		color = (0,0,0)
		self.pygamesurface.lock()
		self.pygamesurface.set_at((self.x, self.y), color)
		self.pygamesurface.unlock()

	def step(self, mouseX, mouseY):
		# because randomness happens in x,y axes
		# there are 9 choices: 2 vertical, 2 horizontal, 4 diagonal, no motion)
		
		# probabilities:
		r = random.random() # float between 0 and 1 (exclusive)

		#distance, (xdir, ydir) = self.get_direction(mouseX, mouseY)

		orgx = self.x
		orgy = self.y

		if r < 0.7:
			print('move randomly in any direction')
			# Move mouse randomly in any direction
			stepx = random.randint(-1, 1) # left, stay, right
			stepy = random.randint(-1, 1) # up, stay, down
		else:
			print('move mostly right and down')
			# Move mouse mostly right or down
			stepx = random.randint(0, 1) # stay, right
			stepy = random.randint(0, 1) # stay, down
		
		# update position based on random step selection
		self.x += stepy 
		self.y += stepx
