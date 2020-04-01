import pygame as pg


pg.init()
screen = pg.display.set_mode((640, 480))
clock = pg.time.Clock()

# I draw the ellipse onto this surface.
surf = pg.Surface((260, 160), pg.SRCALPHA)
pg.draw.ellipse(surf, (0, 128, 255), (0, 0, 260, 160))
# Another per-pixel alpha surface, filled with a translucent color.
alpha_surf = pg.Surface(surf.get_size(), pg.SRCALPHA)
alpha_surf.fill((255, 255, 255, 120))  # Set the alpha here (4th argument).
# Blit the alpha_surf onto the surface and pass the BLEND_RGBA_MULT flag.
surf.blit(alpha_surf, (0, 0), special_flags=pg.BLEND_RGBA_MULT)
rect = surf.get_rect()


running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEMOTION:
            rect.topleft = event.pos

    screen.fill((64, 64, 64))
    #pg.draw.rect(screen, (128, 255, 0), (200, 200, 100, 100))
    screen.blit(surf, rect)
    pg.display.flip()
    clock.tick(60)