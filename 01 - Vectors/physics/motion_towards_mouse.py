# mover class
import random, pygame
from physics.vector import PVector


class Mover:

    def __init__(self, surface):
        self.width, self.height = surface.get_size()
        self.surface = surface
        #self.mouseX, self.mouseY = pygame.mouse.get_pos()
        self.location = PVector(self.width//2, self.height//2)
        self.velocity = PVector(0, 0)
        self.acceleration = PVector(-0.001, 0.01) # key!
        self.topspeed = 10 # limits magnitude of the velocity

    # velcity changes by acceleration and is limited by topspeed
    def update(self, mouseX, mouseY):
    	# 1. calculate a vector that points from obj to target location
    	# 2. Normalize the vector (reducing its length to 1)
    	# 3. Scale that vector to an appropriate value (by multiplying it by some value)
    	# 4. Assign that vector to acceleration
        self.mouse = PVector(mouseX, mouseY)
        dir = self.mouse - self.location # 1. compute direction
        dir = dir.normalize() # 2. normalize
        dir *= 0.5 # 3. scale
        self.acceleration = dir # 4. accelerate

        self.velocity += self.acceleration
        self.velocity = self.velocity.limit(self.topspeed)
        self.location += self.velocity

    # same as original motion class
    def display(self):
        stroke = (0,0,0)
        fill = (175, 175, 175)
        diam = 32
        dimensions = (self.location.values[0], self.location.values[1], diam, diam)
        pygame.draw.ellipse(self.surface, fill, dimensions) # fille
        pygame.draw.ellipse(self.surface, stroke, dimensions, 2)  # stroke

    # same as original motion class
    def checkEdges(self):
        if self.location.values[0] > self.width:
            self.location.values[0] = 0
        elif self.location.values[0] < 0:
            self.location.values[0] = self.width

        if self.location.values[1] > self.height:
            self.location.values[1] = 0
        elif self.location.values[1] < 0:
            self.location.values[1] = self.height
