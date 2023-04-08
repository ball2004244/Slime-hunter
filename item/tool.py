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
        player.image = pg.Surface((self.width, self.height))
        player.image.fill(self.color)
        player.rect = player.image.get_rect()
        player.rect.x = self.rect.x
        player.rect.y = self.rect.y

class WoodenPickaxe(Tool):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, width, height, color)
        self.name = 'wooden_pickaxe'
        self.tag = 'tool'
        self.mining_power = 1


