import pygame as pg
from pygame.locals import *

pg.init()

# create an abstract Item class as a sprite


class Item(pg.sprite.Sprite):
    def __init__(self, x, y, width, height, color=(0, 0, 0)):
        super().__init__()
        self.image = pg.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height
        self.pickup_state = True

        self.color = color

        self.tag = 'item'
        self.name = 'item'

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def pickup(self):
        self.pickup_state = False
        self.kill()

    def move(self):
        # move to the right 20 units
        self.rect.x += 20

    def get_save_data(self):
        # get position first
        save_dict = {'name': self.name, 'x': self.rect.x, 'y': self.rect.y,
                     'width': self.width, 'height': self.height, 'color': self.color, 'picked_up': self.pickup_state}

        return save_dict

    def load_data(self, save_data):
        self.rect.x = save_data['x']
        self.rect.y = save_data['y']
        self.width = save_data['width']
        self.height = save_data['height']
        self.rect.width = self.width
        self.rect.height = self.height
        self.color = save_data['color']

        self.pickup_state = save_data['picked_up']
        if not self.pickup_state:
            self.kill()

        
