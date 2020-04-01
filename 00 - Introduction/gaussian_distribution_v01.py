import pygame, random
import numpy as np

# target std and mean
sd = 60
mean = 320
# get a normal distribution with mean 0 and STD 1:
mu0, sigma1, population = 0, 1, 360 # mean, standard deviation, pop size
gaussian = np.random.normal(mu0, sigma1, population) # get dataset
# get random num from distribution
index = int(random.randrange(population))
num = gaussian[index]

# adjust to the number we want based on target std and mean:
x = sd * num + mean
print('num: ', num, ' x:', x)
