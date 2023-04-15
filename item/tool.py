import pygame as pg
from pygame.locals import *
from item.item import Item

pg.init()

class Tool(Item):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, width, height, color)
        self.name = 'tool'
        self.tag = 'tool'
        self.durability = 100
        self.mining_power = 0

    def equip(self, player):
        super().equip(player)
        self.rect.x = player.rect.x
        self.rect.y = player.rect.y


pickaxe_image = pg.image.load('asset/image/pickaxe.png')
class WoodenPickaxe(Tool):
    def __init__(self, x, y, width, height, color=(255, 0, 255)):
        super().__init__(x, y, width, height, color)

        self.image = pickaxe_image
        self.image = pg.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.name = 'wooden_pickaxe'
        self.tag = 'tool'
        self.mining_power = 1

        self.color = (255, 0, 255)


