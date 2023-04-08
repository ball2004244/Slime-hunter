# process the user keyboard + mouse input
import pygame as pg
from pygame.locals import *
import sys

pg.init()

class Control:
    def __init__(self, player, inventory):
        self.player = player
        self.inventory = inventory

    def move(self, keys):
        # moving the player
        
        if keys[K_UP] or keys[K_w]:
            self.player.move_up()
        if keys[K_DOWN] or keys[K_s]:
            self.player.move_down()
        if keys[K_LEFT] or keys[K_a]:
            self.player.move_left()
        if keys[K_RIGHT] or keys[K_d]:
            self.player.move_right()

        # running the player
        if keys[K_LCTRL]:
            self.player.run_state = True
        else:
            self.player.run_state = False

        self.player.run()

    def mouse_check(self, event, player_group, enemy_group, item_group):
        # check collision between player and enemy
        if event.button == 1:
            collide_list = pg.sprite.groupcollide(player_group, enemy_group, False, False)
            if collide_list:
                enemy = collide_list[self.player][0]
                self.player.attack(enemy)

        # check collision between player and item
        if event.button == 3:
            collide_list = pg.sprite.groupcollide(player_group, item_group, False, False)
            if collide_list:
                item = collide_list[self.player][0]
                self.player.pickup(self.inventory, item)
    
    def open_inventory(self, event):
        if event.key == K_i:
            self.inventory.open_inventory()        

    def event_loop(self, player_group, item_group, enemy_group):   
        keys = pg.key.get_pressed()
        self.move(keys)

        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()

            elif event.type == KEYDOWN:
                self.open_inventory(event)

            elif event.type == MOUSEBUTTONDOWN:
                self.mouse_check(event, player_group, enemy_group, item_group)
                