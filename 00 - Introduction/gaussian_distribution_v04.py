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
HEIGHT = 480
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



# SETUP
# starting background
background = (0,0,0)
#screen.fill(background)
# custom objs

# functions
def draw():

	# get a normal distribution:
	mean, sd, population = 0, 1, WIDTH # mean, standard deviation, pop size
	gaussian = np.random.normal(mean, sd, population) # make dataset
	# get random num from distribution
	index = int(random.randrange(population))
	num = gaussian[index]
	# normalized num to mean 320 and std 60:
	mean, sd = 320, 60
		# -WIDTH//4 is my addition to correct skewed position 
		# don't know why this doesn't work as in the processing tutorial
	x = sd * num + mean - WIDTH//4 
	print('index: ', index, 'x: ', x)
	
	# TRANSPARENT ELLIPSE
	# 1. make exclusive ellipse surface
	ellipse_surf = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
	ellipse_surf_size = (WIDTH, HEIGHT)
	# 2. draw ellipse
	ellipse_rect = (x, 180, 16, 16) # make rect
	pygame.draw.ellipse(ellipse_surf, ellipse_fill, ellipse_rect) # draw ellipse on rect
	# 3. make alpha surf
	alpha_surf = pygame.Surface(ellipse_surf_size, pygame.SRCALPHA)
	# 4. fill surf -> SET ALPHA HERE!
	alpha_surf.fill(alpha_white)

	# 5. blit ellipse surf unto alpha surf
	ellipse_surf.blit(alpha_surf, (x, 0), special_flags=pygame.BLEND_RGBA_MULT)
	# 6. blit alpha surf unto screen 
	screen.blit(ellipse_surf, ellipse_rect)


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