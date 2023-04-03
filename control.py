# process the user keyboard + mouse input
import pygame as pg
from pygame.locals import *
import sys

pg.init()

class Control:
    def __init__(self, player):
        self.player = player

    def move(self):
        # moving the player
        keys = pg.key.get_pressed()
        if keys[K_UP] or keys[K_w]:
            self.player.move_up()
        if keys[K_DOWN] or keys[K_s]:
            self.player.move_down()
        if keys[K_LEFT] or keys[K_a]:
            self.player.move_left()
        if keys[K_RIGHT] or keys[K_d]:
            self.player.move_right()

    def mouse_check(self, event, item_list, enemy_list):
        # check if the mouse is clicked
        for enemy in enemy_list:
            if event.button == 1:
                self.player.attack(enemy)

        for item in item_list:
            if event.button == 3:
                self.player.pickup(item)
                item.pickup()


    def event_loop(self, item_list, enemy_list):
        self.move()
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                self.mouse_check(event, item_list, enemy_list)
                