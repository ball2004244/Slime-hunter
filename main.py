import pygame as pg
from pygame.locals import *
import sys
from setup import screen_setup

# create a simple pygame window
pg.init()

screen_setup()

# main game loop
while True:
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()

    pg.display.update()




