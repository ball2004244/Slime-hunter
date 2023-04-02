import pygame as pg
from pygame.locals import *
from setup import Screen, COLOR, screen_setup
from control import Control
from entity.player import Player
from entity.enemy import Slime

# create a simple pygame window
pg.init()

# set up the window
screen_setup()

# create instances before loop
player = Player(100, 100, 50, 50, COLOR['green'])
slime = Slime(200, 200, 50, 50, COLOR['red'])

control = Control(player)
# main game loop
while True:
    # fill screen with white
    Screen.fill(COLOR['white'])

    player.draw(Screen)
    slime.draw(Screen)

    # process the user keyboard + mouse input
    control.event_loop()            

    pg.display.update()




