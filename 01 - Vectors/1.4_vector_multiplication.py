#main.py
# https://devdocs.io/pygame/

# import external modules
import pygame, random, sys, math
from pygame.locals import *
# import local scripts
from physics.vector import PVector

# initialize pygame
pygame.init()

# Window title
TITLE = "1.4 Multiplying a vector"
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
framerate = 24
clock = pygame.time.Clock()


# SETUP
# =========================================================================
# starting background

# custom objs

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

	mouseX, mouseY = pygame.mouse.get_pos()

	background = (255, 255, 255) # background should be white to see black line
	screen.fill(background)

	mouse = PVector(mouseX, mouseY)
	center = PVector(WIDTH//2, HEIGHT//2)

	mouse *= 0.5 # Multiplying a vector!
				# the vector is now half its original size (multiplied by 0.5)

	# ----------------------------------------
	# translate: 3 steps
	temp_surf = screen.copy() # 1. copy screen
	screen.fill(background)  # 2. fill the screen with whatever you want to take the place of what was there before
	screen.blit(temp_surf,(WIDTH//2,HEIGHT//2)) # 3. blit translated surf to new location
	# one line in processing: translate(width/2,height/2);
	# -----------------------------------------

	print('mouse.values[0], mouse.values[1]')
	print(mouse.values[0], mouse.values[1])
	print(int(mouse.values[0]), int(mouse.values[1]))

	# Draw a line to represent the vector:
	# line: surface, color, point1 (x, y), point 2 (x, y)
	line_color = (0,0,0)
	pygame.draw.line(screen, line_color, (0, 0), (int(mouse.values[0]), int(mouse.values[1])))

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
