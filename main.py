from __init__ import *

# load_game()

while True:
    gameplay.game_loop()

# main game loop
# while True:
#     # fill screen with white
#     SCREEN.fill(COLOR['white'])

#     gamemap.render(SCREEN)

#     player_group.draw(SCREEN)
#     enemy_group.draw(SCREEN)
#     item_group.draw(SCREEN)
#     block_group.draw(SCREEN)

#     # show status
#     hotbar.draw(SCREEN)
#     show_hp(SCREEN)

#     # slime1.random_movement(movement, camera)

#     # process the user keyboard + mouse input
#     control.event_loop(player_group, item_group, enemy_group, block_group)            

#     camera.update(gamemap)
    
#     # the save time is 20s
#     auto_save = save_game(auto_save)
    
#     # save_game(auto_save - 18000)
#     fps_clock.display_fps(SCREEN)
#     pg.display.update()

