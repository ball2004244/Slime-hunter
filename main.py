import pygame as pg
from pygame.locals import *
from setup import SCREEN, COLOR, window_setup, FPS_clock
from control import Control
from character.player import Player
from character.enemy import Slime
from item.apple import Apple

# create a simple pygame window
pg.init()

# set up the window
window_setup()
fps_clock = FPS_clock()

# create instances before loop
player = Player(100, 100, 70, 70, COLOR['green'])
slime = Slime(200, 200, 100, 100, COLOR['gray'])
apple = Apple(300, 300, 30, 30, COLOR['red'])
apple2 = Apple(400, 400, 30, 30, COLOR['red'])
control = Control(player)

item_list = [apple, apple2]
enemy_list = [slime]

# create pygame sprite groups
item_group = pg.sprite.Group()
enemy_group = pg.sprite.Group()

# loop through the item list and add them to the item group
for item in item_list:
    item_group.add(item)

# loop through the enemy list and add them to the enemy group
for enemy in enemy_list:
    enemy_group.add(enemy)
# main game loop
while True:
    # fill screen with white
    SCREEN.fill(COLOR['white'])

    player.draw(SCREEN)
    slime.draw(SCREEN)

    item_group.draw(SCREEN)

    # process the user keyboard + mouse input
    control.event_loop(item_list, enemy_list)            

    fps_clock.display_fps(SCREEN)
    pg.display.update()
