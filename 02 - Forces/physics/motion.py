# mover class
import random, pygame
from physics.vector import PVector


class Mover:

    def __init__(self, surface):
        self.width, self.height = surface.get_size()
        self.surface = surface
        self.location = PVector(random.randrange(self.width), random.randrange(self.height))
        speed = 3
        self.velocity = PVector(random.randrange(-speed, speed), random.randrange(-speed, speed))

    def update(self):
        self.location += self.velocity

    def display(self):
        stroke = (0,0,0)
        fill = (175, 175, 175)
        diam = 32
        dimensions = (self.location.values[0], self.location.values[1], diam, diam)
        pygame.draw.ellipse(self.surface, fill, dimensions) # fille
        pygame.draw.ellipse(self.surface, stroke, dimensions, 2)  # stroke

    def checkEdges(self):
        if self.location.values[0] > self.width:
            self.location.values[0] = 0
        elif self.location.values[0] < 0:
            self.location.values[0] = self.width

        if self.location.values[1] > self.height:
            self.location.values[1] = 0
        elif self.location.values[1] < 0:
            self.location.values[1] = self.height
