#main.py
# https://devdocs.io/pygame/

# import external modules
import pygame, random, sys
from pygame.locals import *
# import local scripts
from physics.vector import PVector
from physics.forces import Mover

# initialize pygame
pygame.init()

# Window title
TITLE = "2.3 Gravity scaled by mass"
pygame.display.set_caption(TITLE)

# screen
WIDTH = 640
HEIGHT = 360
screen = pygame.display.set_mode((WIDTH,HEIGHT))

# Key controls
pressed_key = []

# quitting msg
quitting_message = 'User is quitting the app'

# Clock obj -> to keep track of FPS
framerate = 60
clock = pygame.time.Clock()


# SETUP
# =========================================================================
# starting background

# custom objs
# initialized 100 random mover objects with with random mass and all starting at 0,0
movers = [Mover(screen, random.uniform(0.3, 5), 0, 0) for _ in range(100)] # 20 mover objects in a list
# NOTE: in pygame, the float range won't work when m < 0.3. In forces.py, line 39,
#        the second ellipse has a strokeWeight of 2 (last argument)
# 		for m to be < 0.3, the strokeWeight must be 1.
#		pygame only takes ints for pixel data (e.g. strokeweight, primitive's size, or position)
# =========================================================================

# Functions
def event_handler(): # requires importing locals
	# EVENTS - cannot be placed in a function to be called here
	for event in pygame.event.get(): #all events in pygame
		if event.type == QUIT: # clicking QUIT button (X)
			print(quitting_message)
			running = False # stop running
			pygame.quit() # terminate pygame functionality
			sys.exit() # terminate program
		if event.type == KEYDOWN:
			pressed_key.append(pygame.key.name(event.key)) # pressed_key must be a list for the following to work
			if event.key == K_LALT or event.key == K_F4:
				print(quitting_message)
				running = False # stop running
				pygame.quit() # terminate pygame functionality
				sys.exit() # terminate program

# DRAW
# =========================================================================
def draw():
	global mouseX, mouseY

	background = (255, 255, 255)
	screen.fill(background)

	# Make up forces
	wind = PVector(0.001, 0)

	# loop through all objects and apply both forces to each object
	for i, mover in enumerate(movers):
		m = mover.mass
		gravity = PVector(0, 0.01*m) # scaling gravity by mass to be more accurate
		mover.applyForce(wind)
		mover.applyForce(gravity)

		mover.update()
		mover.display()
		mover.checkEdges()

# =========================================================================

# MAIN LOOP

running = True

while running:

	# MOUSE
	mouseX, mouseY = pygame.mouse.get_pos()
	event_handler()


	# DRAW
	draw()


	# Set FPS
	clock.tick(framerate)
	# Update screen: last line of loop. Fires animation
	pygame.display.update()
