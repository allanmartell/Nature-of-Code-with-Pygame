#main.py
# https://devdocs.io/pygame/

# import external modules
import pygame, random, sys
from pygame.locals import *
from noise import *

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


# GLOBAL

# ellipse vars
ellipse_size = 16
ellipse_fill = (100,100,100)
ellipse_void = (255,255,255)
stroke = 6

# perlin noise:
	# https://medium.com/@yvanscher/playing-with-perlin-noise-generating-realistic-archipelagos-b59f004d8401
# REQUIRED
scale = random.random() # determines at what distance to view the noisemap.
octaves = 6 # levels of detail you want you perlin noise to have.
lacunarity = 0.5 # how much detail is added or removed at each octave (adjusts frequency).
# OPTIONAL:
persistence = 2.0 # how much each octave contributes to the overall shape (adjusts amplitude).

# functions
def linearConversion(OldValue, OldRange, NewRange):
	OldMin, OldMax = OldRange
	NewMin, NewMax = NewRange
	OldRange = (OldMax - OldMin)  
	NewRange = (NewMax - NewMin)  
	NewValue = (((OldValue - OldMin) * NewRange) / OldRange) + NewMin
	return NewValue

def draw():
	global scale

	screen.fill(background)

	# explanation of perlin noise module in python:
	# https://medium.com/@yvanscher/playing-with-perlin-noise-generating-realistic-archipelagos-b59f004d8401
	#n = pnoise1(scale, octaves=octaves, lacunarity=lacunarity, persistence=persistence, base=0)
	
	nx = pnoise1(scale, octaves=octaves, lacunarity=lacunarity)
	print('nx: ', nx) 
	x = linearConversion(nx, (-1, 1), (0, WIDTH))
	print('x: ', x)
	
	# stroke
	ellipse_stroke = pygame.Rect(x-stroke//2, 180-stroke//2, ellipse_size+stroke, ellipse_size+stroke)
	pygame.draw.ellipse(screen, ellipse_void, ellipse_stroke)
	# ellipse
	ellipse_rect = pygame.Rect(x, 180, ellipse_size, ellipse_size)
	pygame.draw.ellipse(screen, ellipse_fill, ellipse_rect)
	
	scale += 0.01




# SETUP
# starting background
background = (0, 0, 0)
screen.fill(background)
# custom objs

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