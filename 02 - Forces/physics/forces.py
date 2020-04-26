# mover class
import random, pygame
from physics.vector import PVector


class Mover:

    def __init__(self, surface, m, x, y):

        self.mass = m # add mass!

        # PREVIOUS STUFF
        self.surface = surface
        self.width, self.height = surface.get_size()
        self.size = 16
        self.diameter = self.size*self.mass

        self.location = PVector(y, x)
        self.velocity = PVector(0, 0)
        self.acceleration = PVector(0, 0)

    # Newton's second law
    def applyForce(self, force): # force is a PVector obj
        f = force/self.mass # receive a force, divide by mass, and
        self.acceleration += f # add to acceleration

    # Motion 101 from ch. 1
    def update(self):
        self.velocity += self.acceleration # Velocity changes by acceleration
        self.location += self.velocity # Location changes by velocity
        self.acceleration *= 0 # now add clearing the acceleration each time!

    # same as original motion class
    def display(self): # display mover
        stroke = (0,0,0)
        fill = (175, 175, 175)
        size = 16
        # scale the diameter (aka size) according to mass
        dimensions = (self.location.values[0], self.location.values[1], self.mass*size, self.mass*size)
        pygame.draw.ellipse(self.surface, fill, dimensions) # filled
        pygame.draw.ellipse(self.surface, stroke, dimensions, 2)  # stroke

    # somehwhat arbitrarily, we are deciding that an object bounces
    # when it hits the edges of the window
    def checkEdges(self):
        if self.location.values[0] > self.width:
            self.location.values[0] = self.width
            self.velocity.values[0] *= -1
        elif self.location.values[0] < 0:
            self.velocity.values[0] *= -1
            self.location.values[0] = 0

        # Even though we said that we shouldn't touch velocity and Location# directly
        # there are exceptions. Here, we are doing so as a quick and easy way to reverse
        # the direction of our object when it reaches the edge.
        if self.location.values[1] > (self.height):
            self.velocity.values[1] *= -1
            self.location.values[1] = self.height
