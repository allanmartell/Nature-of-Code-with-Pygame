#main.py

# import external modules
import pygame, random
# import local scripts

# initialize pygame
pygame.init()

# Window title
TITLE = "Random number distribution"
pygame.display.set_caption(TITLE)

# screen
WIDTH = 640
HEIGHT = 260
screen = pygame.display.set_mode((WIDTH,HEIGHT))

# Key controls
pressed_key = []

# quitting msg
quitting_message = 'User is quitting the app'

# Clock obj -> to keep track of FPS
framerate = 24
clock = pygame.time.Clock()

# Global vars
randomCounts = [] # keep track of how often random numbers are picked
numOfBars = 20
growthRate = 1

# JAVA WAY -> Requires more other below
#for i in range(numOfBars):
	#randomCounts.append(0) # you need all slots already set and ready to be assigned

index = None

# SETUP
# starting background
background = (255, 255, 255)
screen.fill(background)
# custom objs

# Functions - using them is more pythonic, I think

# Generate a random starting height for all bars
def barsHeight():
	
	# if list is empty fill with random nums and assing index
	if len(randomCounts) == 0:
		for i in range(numOfBars):
			index = random.randrange(0, numOfBars)
			randomCounts.append(index)
	# if list is filled, just assign index
	else:
		index = random.randrange(0, len(randomCounts))

	# Increase bar's height
	randomCounts[index] += growthRate

def drawRects():
	stroke = (0,0,0)
	fill = (175,175,175)
	w = WIDTH//len(randomCounts)

	# Graphing the results
	for x, item in enumerate(randomCounts):
		
		# setting rect parameters
		rectX = x * w # rect x is a multiple of the screen Width
		rectY = HEIGHT - randomCounts[x] # rect y is based on screen Height, and it increases to match H
		rectW = w - 1 # rect w is fixed
		rectH = randomCounts[x] # rectH increases + 1 every frame
		
		# define rects' sizes
		rect = pygame.Rect(rectX, rectY, rectW, rectH)
		# draw rects
		pygame.draw.rect(screen, fill, rect)
		# draw strokes
		pygame.draw.rect(screen, stroke, rect, 2)


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

	# JAVA WAY
	# pick a random number and increase the count
	#index = random.randrange(0, len(randomCounts))

	# PYTHONIC WAY - I think
	barsHeight()
	drawRects()

	# Set FPS
	clock.tick(framerate)
	# Update screen: last line of loop. Fires animation
	pygame.display.update()