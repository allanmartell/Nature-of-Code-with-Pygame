import pygame, random
import numpy as np


# get a normal distribution:
mu, sigma, population = 320, 60, 360 # mean, standard deviation, pop size
gaussian = np.random.normal(mu, sigma, population) # get dataset
# get random num from distribution
index = int(random.randrange(population))
num = gaussian[index]

# adjust to the number we want based on target std and mean:
