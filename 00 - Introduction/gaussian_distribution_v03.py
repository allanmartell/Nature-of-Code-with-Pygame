#main.py

# import external modules
import pygame, random
import numpy as np
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


# GLOBAL VARS
# drawing vars
white = (255, 255, 255)


# SETUP
# starting background
background = (0,0,0)
screen.fill(background)
# custom objs

# functions
def draw():
	# get a normal distribution:
	mu, sigma, population = 320, 60, 360 # mean, standard deviation, pop size
	gaussian = np.random.normal(mu, sigma, population) # get dataset
	# get random num from distribution
	index = int(random.randrange(population))
	x = int(gaussian[index])
	print(x)
	# alpha_screen to draw ellipse
	alpha_screen = pygame.Surface((16, 16))
	alpha_screen.set_alpha(10)
	alpha_screen.fill(white)
	rect = pygame.Rect(x, 180, 16, 16) # size of rect on alpha mode
	pygame.draw.ellipse(alpha_screen, white, rect)
	screen.blit(alpha_screen, (x,180))

# MAIN LOOP

running = True

while running:
	
	# MOUSE
	mouseX, mouseY = pygame.mouse.get_pos()

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
	draw()


	# Set FPS
	clock.tick(framerate)
	# Update screen: last line of loop. Fires animation
	pygame.display.update()