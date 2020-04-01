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

	def get_direction(self, mouseX, mouseY):
		# retrieve distance from mouse (dist) and direction (xd,yd)
		p1 = (self.x, self.y)
		p2 = (mouseX, mouseY) 

		distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )
		
		xd = p2[0]-p1[0]
		yd = p2[1]-p1[1]

		if xd < 0:
			xdirection = -1 # mouse is left
		else:
			xdirection = 1 # mouse is right
		if yd < 0:
			ydirection = -1 # mouse is above
		else:
			ydirection = 1 # mouse is below

		return distance, (xdirection, ydirection)

	def step(self, mouseX, mouseY):
		# because randomness happens in x,y axes
		# there are 9 choices: 2 vertical, 2 horizontal, 4 diagonal, no motion)
		
		# probabilities:
		r = random.random() # float between 0 and 1 (exclusive)

		distance, (xdir, ydir) = self.get_direction(mouseX, mouseY)

		orgx = self.x
		orgy = self.y

		if r < 0.2:
			print('approach mouse')
			self.x += xdir
			self.y += ydir
		else:
			print('random move')
			# Move mouse randomly in any direction
			stepx = random.randint(-1, 1) # left, stay, right
			stepy = random.randint(-1, 1) # up, stay, down
			# update position based on random step selection
			self.x += stepy 
			self.y += stepx

		aftx = self.x
		afty = self.y

		