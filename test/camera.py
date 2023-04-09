# create a camera class to follow the player
# the camera will move if the user touch the padding
# character/player.py
# setup.py <-> config.cfg
# main.py
# __init__.py
# map/map.py
import pygame as pg
from pygame.locals import *

pg.init()

class Camera:
    def __init__(self, player, screen_width, screen_height, map_width, map_height):
        self.player = player
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.map_width = map_width
        self.map_height = map_height


        self.padding = 100
        self.padding_top = self.padding
        self.padding_left = self.padding
        self.padding_right = self.screen_width - self.padding
        self.padding_bottom = self.screen_height - self.padding

        self.speed = self.player.default_speed


    def move_top(self, _map):
        if self.player.rect.y <= self.padding_top:
            self.player.top_transition = True
            _map.y += self.speed
            return
        
        self.player.top_transition = False

    def move_bottom(self, _map):
        if self.player.rect.y >= self.padding_bottom:
            self.player.bottom_transition = True
            _map.y -= self.speed
            return
        
        self.player.bottom_transition = False

    def move_left(self, _map):
        if self.player.rect.x <= self.padding_left:
            self.player.left_transition = True
            _map.x += self.speed
            return
        
        self.player.left_transition = False

    def move_right(self, _map):
        if self.player.rect.x >= self.padding_right:
            self.player.right_transition = True
            _map.x -= self.speed
            return
        
        self.player.right_transition = False

    def transition(self, _map):
        self.speed = self.player.speed
        self.move_top(_map)
        self.move_bottom(_map)
        self.move_left(_map)
        self.move_right(_map)
class Map:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        # import image
        self.image = pg.image.load('background.jpg')
        self.image = pg.transform.scale(self.image, (self.width, self.height))

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))