#main.py
# https://devdocs.io/pygame/

# import external modules
import pygame, random, sys
from pygame.locals import *
# import local scripts

# initialize pygame
pygame.init()

# Window title
TITLE = "Program's title"
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
clouding = True


# SETUP
# starting background
background = (0, 0, 0)
screen.fill(background)
# custom objs

# Functions 

def make_clouds():
	global clouding
	if clouding:
		for x in range(screen.get_width()):
			for y in range(screen.get_height()):
				bright = random.randrange(255)
				pix_color = (bright, bright, bright)
				screen.set_at((x, y), pix_color)
	clouding = False

def switch_clouding():
	global clouding
	clouding = not clouding

def draw():
	make_clouds()
	

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
			if event.key == K_r:
				switch_clouding()

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