# process the user keyboard + mouse input
import pygame as pg
from pygame.locals import *
import sys

pg.init()

class Control:
    def __init__(self, player, inventory, hotbar):
        self.player = player
        self.inventory = inventory
        self.hotbar = hotbar
        self.pause_state = False

    def update_mouse_rect(self, x, y):
        # create a rect for mouse
        self.mouse_rect = pg.Rect(x, y, 1, 1)

    def pause(self, pause_screen):
        # pause the game
        if not self.pause_state:
            return
        
        pause_screen.draw()   


    def pause_logic(self, pause_screen):
        # check collision between mouse and button
        # use colliderect to check collision between mouse and button
        if pause_screen.button1.rect.colliderect(self.mouse_rect):
            pause_screen.button1.activate()
        if pause_screen.button2.rect.colliderect(self.mouse_rect):
            pause_screen.button2.activate()

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

    def mouse_check(self, event, player_group, enemy_group, item_group, block_group, pause_screen):

        # check collision between mouse and button
        if event.button == 1:
            if self.pause_state:
                self.pause_logic(pause_screen)

        # check collision between player and enemy
        if event.button == 1:
            for enemy in enemy_group:
                if self.player.hitbox.colliderect(enemy.rect):
                 self.player.attack(enemy, self.hotbar.current_item(), self.inventory)

        # check collision between player and block
        if event.button == 1:
            collide_list = pg.sprite.groupcollide(player_group, block_group, False, False)
            if collide_list:
                block = collide_list[self.player][0]
                self.player.break_block(self.hotbar.current_item(), block, self.inventory)

        # check collision between player and item
        if event.button == 3:
            collide_list = pg.sprite.groupcollide(player_group, item_group, False, False)
            if collide_list:
                item = collide_list[self.player][0]
                self.player.pickup(self.inventory, item)
         

    def event_loop(self, player_group, item_group, enemy_group, block_group, pause_screen):
        # update mouse rect
        mouse_pos = pg.mouse.get_pos()
        self.update_mouse_rect(mouse_pos[0], mouse_pos[1])

        # check collision between player and enemy
        collide_list = pg.sprite.groupcollide(player_group, enemy_group, False, False)
        if collide_list:
            enemy = collide_list[self.player][0]

            enemy.attack(self.player)

        # move the player
        keys = pg.key.get_pressed()
        self.move(keys)

        #  pause screen
        self.pause(pause_screen)

        # check keyboard input
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()

            elif event.type == KEYDOWN:
                # toggle pause
                if event.key == K_p:
                    if self.pause_state:
                        self.pause_state = False
                    else:
                        self.pause_state = True

            elif event.type == KEYDOWN:
                # open inventory
                if event.key == K_i:
                    self.inventory.open_inventory() 

                # select item in the hotbar
                elif event.key in [K_1, K_2, K_3, K_4]:
                    self.hotbar.select_slot(event.key - 48)


            elif event.type == MOUSEBUTTONDOWN:
                self.mouse_check(event, player_group, enemy_group, item_group, block_group, pause_screen)
