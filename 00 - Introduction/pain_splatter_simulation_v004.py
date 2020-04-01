#main.py

# import external modules
import pygame, random, sys
import numpy as np
from sklearn.preprocessing import normalize
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
background = (0,0,0)
drop_size = 7
mean, sd = (600, 200) # mean and sd of desired normal distribution
radius = sd/6

# SETUP

screen.fill(background) # -> this line would prevent me from accumulating on screen

# custom objs

# functions

def get_gaussian():
	# make normal distribution: mean 0, sd 1
	mean, sd, population = 0, 1, HEIGHT # mean, standard deviation, pop size
	normal_dist = np.random.normal(mean, sd, population) # make dataset
	return normal_dist


def linearConversion(OldValue, OldRange, NewRange):
	OldMin, OldMax = OldRange
	NewMin, NewMax = NewRange
	OldRange = (OldMax - OldMin)
	NewRange = (NewMax - NewMin)
	NewValue = (((OldValue - OldMin) * NewRange) / OldRange) + NewMin
	return NewValue

def isInside(circle_x, circle_y, rad, x, y):

    # Compare radius of circle
    # with distance of its center
    # from given point
    if ((x - circle_x) * (x - circle_x) +
        (y - circle_y) * (y - circle_y) <= rad * rad):
        return True;
    else:
        return False;

def getColor():

	# get normal distribution
	normal_dist = get_gaussian()

	alpha_color = []
	population = len(normal_dist)

	for i in range(4):
		index = int(random.randrange(population))
		c = normal_dist[index]
		c = int(linearConversion(c, (min(normal_dist), max(normal_dist)), (0, 255)))
		alpha_color.append(c)

	alpha_color = tuple(alpha_color)
	return alpha_color

# get normalized coordinates given: normal distribution, mean, sd
def coordinates(mean, sd):

	# get normal distribution
	normal_dist = get_gaussian()
	# population -> size of distribution
	population = len(normal_dist)

	# get random x, y
	inX = int(random.randrange(population))
	inY = int(random.randrange(population))
	numX = normal_dist[inX]
	numY = normal_dist[inY]

	# normalize x, y to mean and std:
	x = sd * numX + mean
	y = sd * numY + mean

	# normalize X, Y
		# -> without this, coords reproduce bell-shape
		# -> with it, coords mimic paint splash
	normX = (x-min(normal_dist))/(max(normal_dist)-min(normal_dist))
	normY = (y-min(normal_dist))/(max(normal_dist)-min(normal_dist))

	return normX, normY

def far_coordinates(mean, sd, radius):

	normX, normY = coordinates(mean, sd)

	# get normal distribution
	normal_dist = get_gaussian()

	# population -> size of distribution
	population = len(normal_dist)

	# screen center
	cx = (WIDTH//2-min(normal_dist))/(max(normal_dist)-min(normal_dist))
	cy = (HEIGHT//2-min(normal_dist))/(max(normal_dist)-min(normal_dist))

	for i in range(population):
		if isInside(cx, cy, radius, normX, normY):
			inX = int(random.randrange(population))
			numX = normal_dist[inX]
			inY = int(random.randrange(population))
			numY = normal_dist[inY]
			continue
		else:
			return normX, normY
			break

	return normX, normY


def close_coordinates(mean, sd, radius):

	normX, normY = coordinates(mean, sd)

	# get normal distribution
	normal_dist = get_gaussian()
	# population -> size of distribution
	population = len(normal_dist)

	# screen center
	cx = (WIDTH//2-min(normal_dist))/(max(normal_dist)-min(normal_dist))
	cy = (HEIGHT//2-min(normal_dist))/(max(normal_dist)-min(normal_dist))

	for i in range(population):
		if not isInside(cx, cy, radius, normX, normY):
			inX = int(random.randrange(population))
			numX = normal_dist[inX]
			inY = int(random.randrange(population))
			numY = normal_dist[inY]
			continue
		else:
			return normX, normY
			break

	return normX, normY

def draw():
	# probabilities:
	r = random.random() # float between [0 and 1)

	if r < 0.1: # prob that points are close
		#normX, normY = close_coordinates(mean, sd, radius)
		normX, normY = close_coordinates(mean, sd, radius)
	else: # prob that points are far
		normX, normY = far_coordinates(mean, sd, radius)

	# Adjust normalized coordinates to screen centre
	normX += WIDTH//3*1.2
	normY += HEIGHT//3
	normX = int(normX)
	normY = int(normY)

	alpha_color = getColor()

	# TRANSPARENT ELLIPSE
	# 1. make alpha surface (able to hold multiple alpha objs)
	alpha_surf = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
	# 2. draw alpha-colored shape
	#print(normX, normY, drop_size, drop_size)
	ellipse_rect = pygame.Rect(normX, normY, drop_size, drop_size)
	pygame.draw.ellipse(alpha_surf, alpha_color, ellipse_rect)
	# 3. blit alpha surf to screen
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
