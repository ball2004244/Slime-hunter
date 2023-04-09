import pygame as pg
from pygame.locals import *
from setup import SCREEN, COLOR, window_setup, FPS_clock
from __init__ import _map, MAP_WIDTH, MAP_HEIGHT, player_group, camera, control

# create a simple pygame window
pg.init()

# set up the window
window_setup()
fps_clock = FPS_clock()

# import background.jpg and resize it to 1920x1080,

# main game loop
while True:
    # fill screen with white
    SCREEN.fill(COLOR['white'])

    # draw background
    _map.draw(SCREEN)
    player_group.draw(SCREEN)
    
    camera.transition(_map)

    """ enemy_group.draw(SCREEN)
    item_group.draw(SCREEN)
    block_group.draw(SCREEN)

    # show status
    status_bar.show_status(SCREEN, player)
    hotbar.draw(SCREEN)
    show_hp(SCREEN) """

    # process the user keyboard + mouse input"""
    control.event_loop(player_group, None, None, None)         

    fps_clock.display_fps(SCREEN)
    pg.display.update()
