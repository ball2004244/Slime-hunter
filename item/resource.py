import pygame as pg
from pygame.locals import *
from item.item import Item
from setup import COLOR
pg.init()


class Resource(Item):
    def __init__(self, x, y, width, height, stack_capacity=16):
        super().__init__(x, y, width, height, COLOR['black'])
        self.stack_capacity = stack_capacity
        self.pickup_state = False
        
        self.name = 'resource'
        self.tag = 'resource'
        self.quantity = 0

class Wood(Resource):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.name = 'wood'
        self.tag = 'wood'

        # self.image = pg.image.load('assets/wood.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        # draw 2 browns rectangles
        pg.draw.rect(screen, (139, 69, 19), (self.rect.x, self.rect.y, self.rect.width, self.rect.height))
        pg.draw.rect(screen, (139, 69, 19), (self.rect.x + 10, self.rect.y + 10, self.rect.width - 20, self.rect.height - 20))

class Stone(Resource):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.name = 'stone'
        self.tag = 'stone'

        # self.image = pg.image.load('assets/stone.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        # draw 2 grey rectangles
        pg.draw.rect(screen, (105, 105, 105), (self.rect.x, self.rect.y, self.rect.width, self.rect.height))
        pg.draw.rect(screen, (105, 105, 105), (self.rect.x + 10, self.rect.y + 10, self.rect.width - 20, self.rect.height - 20))

class Coin(Resource):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.name = 'coin'
        self.tag = 'coin'

        # self.image = pg.image.load('assets/coin.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        # draw a yellow circle
        pg.draw.circle(screen, (255, 255, 0), (self.rect.x + 10, self.rect.y + 10), 10)