# https://www.reddit.com/r/pygame/comments/9moqsk/drawing_a_transparent_ellipse/

import random
import numpy as np
import pygame as pg


pg.init()
screen = pg.display.set_mode((640, 320))
clock = pg.time.Clock()

x = 0
y = 180

# TRANSPARENT ELLIPSE
# =====================================================
# I draw the ellipse onto this surface.
surf = pg.Surface(screen.get_size(), pg.SRCALPHA)
rect = surf.get_rect()
print('rect: ', rect)
# =====================================================

def draw():

    # get a normal distribution:
    mu, sigma, population = 320, 60, 360 # mean, standard deviation, pop size
    gaussian = np.random.normal(mu, sigma, population) # get dataset
    # get random num from distribution
    index = int(random.randrange(population))
    x = int(gaussian[index])

    # TRANSPARENT ELLIPSE
    # =====================================================
    pg.draw.ellipse(surf, (255, 255, 255), (x, 180, 16, 16))
    # Another per-pixel alpha surface, filled with a translucent color.
    alpha_surf = pg.Surface(surf.get_size(), pg.SRCALPHA)
    alpha_surf.fill((255, 255, 255, 120))  # Set the alpha here (4th argument).
    # Blit the alpha_surf onto the surface and pass the BLEND_RGBA_MULT flag.
    surf.blit(alpha_surf, (x, 0), special_flags=pg.BLEND_RGBA_MULT)
    screen.blit(surf, rect)
    # =====================================================

running = True
while running:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEMOTION:
            pass#rect.topleft = event.pos

    draw()
    #screen.fill((64, 64, 64))
    #pg.draw.rect(screen, (128, 255, 0), (200, 200, 100, 100))
    
    #screen.blit(surf, rect)
    pg.display.update()
    clock.tick(60)