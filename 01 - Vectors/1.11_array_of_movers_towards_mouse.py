#main.py
# https://devdocs.io/pygame/

# import external modules
import pygame, random, sys
from pygame.locals import *
# import local scripts
from physics.vector import PVector
from physics.motion_towards_mouse_v2 import Mover

# initialize pygame
pygame.init()

# Window title
TITLE = "Accelerating towards the mouse"
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
movers = [Mover(screen) for _ in range(20)] # 20 mover objects in a list

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

	for i, mover in enumerate(movers):
		mover.update(mouseX, mouseY)
		mover.checkEdges()
		mover.display()
	#print(f"mover s

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
