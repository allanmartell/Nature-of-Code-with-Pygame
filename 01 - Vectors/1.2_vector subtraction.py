#main.py
# https://devdocs.io/pygame/

# import external modules
import pygame, random, sys, math
from pygame.locals import *
# import local scripts
from vector import *

# initialize pygame
pygame.init()

# Window title
TITLE = "01. Bouncing ball with vectors"
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
	global background, location, velocity, size

	# drawing background every frame helps simulate movement
	screen.fill(background)

	location += velocity # in processing would be location.add(velocity)

	#obj.values[0] == obj.x in Shiffman's book
	#obj.values[1] == obj.y in Shiffman's book

	if location.values[0] > (WIDTH-size+2) or location.values[0] < 0:
		velocity.values[0] *= -1 
	if location.values[1] > (HEIGHT-size+2) or location.values[1] < 0:
		velocity.values[1] *= -1

	erect = pygame.Rect(int(location.values[0]), int(location.values[1]), size, size)
	fill = (175, 175, 175)
	pygame.draw.ellipse(screen, fill, erect)
	

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