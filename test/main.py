import pygame as pg
from pygame.locals import *
from setup import SCREEN, COLOR, window_setup, FPS_clock
from __init__ import *

# create a simple pygame window
pg.init()

# set up the window
window_setup()
fps_clock = FPS_clock()

# main game loop
while True:
    # fill screen with white
    SCREEN.fill(COLOR['white'])

    gamemap.render(SCREEN)
    # draw background
    player_group.draw(SCREEN)
    
    camera.update(gamemap)
    # print(camera.get_pos())
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
