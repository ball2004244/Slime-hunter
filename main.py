import pygame as pg
from pygame.locals import *
from setup import SCREEN, COLOR, window_setup, FPS_clock
from __init__ import *

# create a simple pygame window
pg.init()

# set up the window
window_setup()
fps_clock = FPS_clock()

load_game()

auto_save = pg.time.get_ticks()
# main game loop
while True:
    # fill screen with white
    SCREEN.fill(COLOR['white'])

    gamemap.render(SCREEN)

    player_group.draw(SCREEN)
    enemy_group.draw(SCREEN)
    item_group.draw(SCREEN)
    block_group.draw(SCREEN)

    # show status
    hotbar.draw(SCREEN)
    show_hp(SCREEN)

    # slime1.random_movement(movement, camera)

    # process the user keyboard + mouse input
    control.event_loop(player_group, item_group, enemy_group, block_group)            

    camera.update(gamemap)
    
    auto_save = save_game(auto_save)

    # the save time is 20s
    # save_game(auto_save - 18000)
    fps_clock.display_fps(SCREEN)
    pg.display.update()
