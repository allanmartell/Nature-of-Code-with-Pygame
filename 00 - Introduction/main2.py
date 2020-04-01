#main.py

# import external modules
import pygame, random
# import local scripts
from walker2 import Walker

# A walker that can either move forward, backward or stay put

# initialize pygame
pygame.init()

# Window title
TITLE = "Walker program"
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
# starting background
background = (255, 255, 255)
screen.fill(background)
# make walker obj
w = Walker(screen)


# MAIN LOOP

running = True

while running:

	# EVENTS - cannot be placed in a function to be called here
	for event in pygame.event.get(): #all events in pygame
		if event.type == pygame.QUIT: # clicking QUIT button (X)
			running = False # stop running
			print(quitting_message)
		if event.type == pygame.KEYDOWN:
			pressed_key.append(pygame.key.name(event.key)) # pressed_key must be a list for the following to work
			if event.key == pygame.K_LALT or event.key == pygame.K_F4:
				running = False # stop running
				print(quitting_message)
	
	# DRAW
	w.step()
	w.display()


	# Set FPS
	clock.tick(framerate)
	# Update screen: last line of loop. Fires animation
	pygame.display.update()