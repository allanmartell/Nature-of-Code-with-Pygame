#main.py
# https://devdocs.io/pygame/

# import external modules
import pygame, random, sys
from pygame.locals import *
# import local scripts
from physics.vector import PVector
from controls import matstack as ms

# initialize pygame
pygame.init()

# Window title
TITLE = "1.5 Vector Magnitude"
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
	global mouseX, mouseY

	#ms.reset_mat()

	# background
	background = (255, 255, 255)
	screen.fill(background)

	#print(f"mouseX: {mouseX}, mouseY: {mouseY}")
	mouse = PVector(mouseX, mouseY)
	center = PVector(WIDTH//2, HEIGHT//2)
	mouse -= center

	# line
	line_color = (0,0,0)
	pygame.draw.line(screen, line_color, (0, 0), (int(mouse.values[0]), int(mouse.values[1])))

	# anything before this line will be translated
	# ----------------------------------------
	# translate: 3 steps
	temp_surf = screen.copy() # 1. copy screen
	screen.fill(background)  # 2. fill the screen with whatever you want to take the place of what was there before
	screen.blit(temp_surf,(WIDTH//2,HEIGHT//2)) # 3. blit translated surf to new location
	# one line in processing: translate(width/2,height/2);
	# -----------------------------------------

	# rect
	m = mouse.mag()
	rect_color = (0,0,0)
	rect_dimensions = (0,0, int(m), 10)
	pygame.draw.rect(screen, rect_color, rect_dimensions)

	# NOTES:
	# script won't run as in original processing sketch 1.5: https://natureofcode.com/book/chapter-1-vectors/
	# in pygame, translating the canvas leads to a mouse position error. Once origin is moved to screen center
	# mouseX and mouseY cannot read the position of the mouse before origin point
	# processing has some solution to this by default. Don't know how to fix in pygame.
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
