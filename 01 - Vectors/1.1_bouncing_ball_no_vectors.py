#main.py
# https://devdocs.io/pygame/

# import external modules
import pygame, random, sys
from pygame.locals import *
# import local scripts

# initialize pygame
pygame.init()

# Window title
TITLE = "01. Bouncing ball no vectors"
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
x = 100
y = 100
xspeed = -1
yspeed = 3.3
radius = 30


# SETUP
# starting background
background = (255, 255, 255)
screen.fill(background)
# custom objs

# Functions 

def draw():
	global x, y, xspeed, yspeed, radius
	# fill background every frame -> shows movement
	screen.fill(background)

	# constant movement
	x += xspeed
	y += yspeed 
	# bouncing behavior
	if x > (WIDTH-radius+2) or x < 0:
		xspeed *= -1
	if y > (HEIGHT-radius+2) or y < 0:
		yspeed *= -1

	erect = pygame.Rect(int(x), int(y), radius, radius)
	fill = (0, 0, 0)
	stroke = (175, 175, 175) 
	# filled ellipse
	pygame.draw.ellipse(screen, stroke, erect)
	# stroke
	pygame.draw.ellipse(screen, fill, erect, 2)
	

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