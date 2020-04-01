#main.py
# https://devdocs.io/pygame/

# import external modules
import pygame, random, sys, math
from pygame.locals import *
# import local scripts
from vector.classes import PVector

# initialize pygame
pygame.init()

# Window title
TITLE = "01. Vector Subtraction"
pygame.display.set_caption(TITLE)

# screen
WIDTH = 640
HEIGHT = 360
screen = pygame.display.set_mode((WIDTH,HEIGHT))

# quitting msg
quitting_message = 'User is quitting the app'

# Clock obj -> to keep track of FPS
framerate = 60
clock = pygame.time.Clock()

# Global vars
mouseX = None
mouseY = None
location = PVector(100, 100)
velocity = PVector(2.5, 5)
size = 16


# SETUP
# starting background
background = (255, 255, 255)
screen.fill(background)
# custom objs

# Functions

def draw():
	global background, location, velocity, size, mouseX, mouseY

	# drawing background every frame helps simulate movement
	screen.fill(background)

	# Two PVectors, one for the mouse location and
	# one for the center of the window
	mouse = PVector(mouseX, mouseY)
	center = PVector(WIDTH/2, HEIGHT/2)

	# PVector subtraction!
	mouse -= center

	# Draw a line to represent the vector
	# ----------------------------------------
	# translate: 3 steps
	temp_surf = screen.copy() # 1. copy screen
	screen.fill(background)  # 2. fill the screen with whatever you want to take the place of what was there before
	screen.blit(temp_surf,(WIDTH//2,HEIGHT//2)) # 3. blit translated surf to new location
	# orginal line in processing: translate(width/2,height/2);
	# -----------------------------------------

	# line
	pygame.draw.line(screen,(0,0,0),(0,0),(mouseX,mouseY))


def event_handler(): # requires importing locals
	pressed_key = []
	# EVENTS - cannot be placed in a function to be called here
	for event in pygame.event.get(): #all events in pygame
		if event.type == QUIT: # clicking QUIT button (X)
			print(quitting_message)
			running = False # stop running
			pygame.quit() # terminate pygame functionality
			sys.exit() # terminate program
		if event.type == KEYDOWN:
			pressed_key.append(pygame.key.name(event.key)) # pressed_key must be a list for the following to work
			print('pressed_key:', pressed_key)
			if 'left alt' in pressed_key and 'f4' in pressed_key:
				print(quitting_message)
				running = False # stop running
				pygame.quit() # terminate pygame functionality
				sys.exit() # terminate program


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
