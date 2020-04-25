# mover class
import random, pygame
from physics.vector import PVector


class Mover:

    def __init__(self, surface):
        self.width, self.height = surface.get_size()
        self.surface = surface
        #self.mouseX, self.mouseY = pygame.mouse.get_pos()
        self.location = PVector(random.randrange(self.width//2), random.randrange(self.height//2))
        self.velocity = PVector(0, 0)
        self.topspeed = 8 # limits magnitude of the velocity

    # velcity changes by acceleration and is limited by topspeed
    def update(self, mouseX, mouseY):
        # Our algorithm for calculating velocity
        # =================================================
        self.mouse = PVector(mouseX, mouseY) # 1 find the vector pointing towards mouse
        dir = self.mouse - self.location
        dir = dir.normalize() # 2. normalize
        dir *= 0.5 # 3 scale
        self.acceleration = dir # 4 set to acceleration

        # 5. Motion 101
        self.velocity += self.acceleration # Velocity changes by acceleration
        self.velocity = self.velocity.limit(self.topspeed)
        self.location += self.velocity # Location changes by velocity

    # same as original motion class
    def display(self): # display mover
        stroke = (0,0,0)
        fill = (175, 175, 175)
        diam = 32
        dimensions = (self.location.values[0], self.location.values[1], diam, diam)
        pygame.draw.ellipse(self.surface, fill, dimensions) # fille
        pygame.draw.ellipse(self.surface, stroke, dimensions, 2)  # stroke

    # what to do with the edges
    def checkEdges(self):
        if self.location.values[0] > self.width:
            self.location.values[0] = 0
        elif self.location.values[0] < 0:
            self.location.values[0] = self.width

        if self.location.values[1] > self.height:
            self.location.values[1] = 0
        elif self.location.values[1] < 0:
            self.location.values[1] = self.height
