# mover class
import random, pygame
from physics.vector import PVector


class Mover:

    def __init__(self, surface):
        self.width, self.height = surface.get_size()
        self.surface = surface
        self.location = PVector(self.width//2, self.height//2)
        self.velocity = PVector(0, 0)
        self.acceleration = PVector(-0.001, 0.01) # key!
        self.topspeed = 10 # limits magnitude of the velocity

    # velcity changes by acceleration and is limited by topspeed
    def update(self):
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
