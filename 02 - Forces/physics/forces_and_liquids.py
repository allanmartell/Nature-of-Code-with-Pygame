# mover class
import random, pygame
from physics.vector import PVector


class Mover:

    def __init__(self, surface, m, x, y):

        self.mass = m # add mass!
        self.size = 16*self.mass

        # PREVIOUS STUFF
        self.surface = surface
        self.width, self.height = surface.get_size()
        self.size = 16
        self.diameter = self.size*self.mass

        self.location = PVector(x, y)
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
        #dimensions = (self.location.values[0], self.location.values[1], self.size, self.size)
        pygame.draw.ellipse(self.surface, fill, dimensions) # filled
        pygame.draw.ellipse(self.surface, stroke, dimensions, 2)  # stroke

    # somehwhat arbitrarily, we are deciding that an object bounces
    # when it hits the edges of the window
    def checkEdges(self):
        if self.location.values[0] > (self.width):
            self.location.values[0] = self.width
            self.velocity.values[0] *= -1
        elif self.location.values[0] < 0:
            self.velocity.values[0] *= -1
            self.location.values[0] = 0

        # Even though we said that we shouldn't touch velocity and Location# directly
        # there are exceptions. Here, we are doing so as a quick and easy way to reverse
        # the direction of our object when it reaches the edge.
        # NOTE: whenever I try to modify the condition that that ball bounces
        #       before disappearing from the bottom corner, there is a glitch.
        #       The ball, rather than bouncing earlier, shrinks
        if (self.location.values[1]) > (self.height):
            self.velocity.values[1] *= -1
            self.location.values[1] = self.height

    def isInside(self, liq):
        # this conditional statement determines if the PVector location is inside
        # the rectangle defined by the Liquid class.
        if self.location.values[0] > liq.x and self.location.values[0] < (liq.x+liq.w) and self.location.values[1] > liq.y and self.location.values[1] < (liq.y+liq.h):
            return True
        else:
            return False

    # apply drag force to the Mover obj
    def drag(self, liq):
        speed = self.velocity.mag() # speed is a scalar, the magnitude of the velocity PVector
        dragMagnitude = liq.c * speed**2 # force magnitude: Cd * v~2~
        drag = self.velocity*-1 # forces direction: -1 * velocity
        drag = drag.normalize()
        drag *= dragMagnitude # finalize the force: magnitude and direction together
        self.applyForce(drag) # apply force to current Mover object


class Liquid:

    # Liquid function includes a variable (_c) defining its coefficient of drag
    def __init__(self, _surf, _x, _y, _w, _h, _c):
        self.surf = _surf
        self.x = _x
        self.y = _y
        self.w = _w
        self.h = _h
        self.c = _c

    def display(self):
        fill = (175, 175, 175)
        dimensions = (self.x, self.y, self.w, self.h)
        pygame.draw.rect(self.surf, fill, dimensions)
