# mover class
import random, pygame
from vector import PVector


class Mover:

    def __init__(self, surface):
        self.width, self.height = surface.get_size()
        self.surface = surface
        self.location = PVector(random.randrange(self.width), random.randrange(self.height))
        self.velocity = PVector(random.randrange(-2, 2), random.randrange(-2, 2))

    def update(self):
        location += velocity

    def display(self):
        stroke = (0,0,0)
        fill = (175, 175, 175)
        dimensions = (location.values[0], location.values[1], 16, 16)
        pygame.draw.ellipse(self.surface, fill, dimensions) # fille
        pygame.draw.ellipse(surface, stroke, dimensions, width=1)  # stroke

    def checkEdges(self):
        if location.values[0] > self.width:
            location.values[0] = 0
        elif location.values[0] < 0:
            location.values[0] = self.width

        if location.values[1] > self.height:
            location.values[1] = 0
        elif location.values[1] < 0:
            location.values[1] = self.height
