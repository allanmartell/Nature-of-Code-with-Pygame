#main.py

# import external modules
import pygame, random, sys
import numpy as np
# import local scripts

# initialize pygame
pygame.init()

# Window title
TITLE = "Program's title"
pygame.display.set_caption(TITLE)

# screen
WIDTH = 640
HEIGHT = 320
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
ellipse_fill = (255, 255, 255)
alpha_white = (255, 255, 255, 120)
drop_size = 5



# SETUP
# starting background
background = (0,0,0)
#screen.fill(background)
# custom objs

# functions
def draw():

	# GET X

	# v.1: mean 0, sd 1 and normalize for custom mean and sd
	# --------------------------------------------------------
	# get a normal distribution:
	mean, sd, population = 0, 1, WIDTH # mean, standard deviation, pop size
	gaussian = np.random.normal(mean, sd, population) # make dataset
	# get random num from distribution
	inX = int(random.randrange(population))
	inY = int(random.randrange(population))
	numX = gaussian[inX]
	numY = gaussian[inY]
	# normalized num to mean 320 and std 60:
	mean, sd = 320, 60
	x = sd * numX + mean
	y = sd * numY + mean
	print('x: ', x, 'y: ', y)

	# v.2: custom mean and sd 
	# --------------------------------------------------------
		# -> x tilts to the right
		# -> don't know why
	#mean, sd, population = 360, 60, WIDTH # mean, standard deviation, pop size
	#gaussian = np.random.normal(mean, sd, population) # make dataset
	#index = int(random.randrange(population))
	#num = gaussian[index]
	#x = num

	# TRANSPARENT ELLIPSE
	# 1. make alpha surface (able to hold multiple alpha objs)
	alpha_surf = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
	# 2. draw alpha-colored shape
	ellipse_rect = pygame.Rect(x, y, drop_size, drop_size)
	pygame.draw.ellipse(alpha_surf, alpha_white, ellipse_rect)
	# 3. blit alpha surf
	alpha_rect = alpha_surf.get_rect()
	screen.blit(alpha_surf, alpha_rect) # surf obj, rect obj


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
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			pressed_key.append(pygame.key.name(event.key)) # pressed_key must be a list for the following to work
			if event.key == pygame.K_LALT or event.key == pygame.K_F4:
				running = False # stop running
				print(quitting_message)
				pygame.quit()
				sys.exit()
	

	# DRAW
	draw()


	# Set FPS
	clock.tick(framerate)
	# Update screen: last line of loop. Fires animation
	pygame.display.update()