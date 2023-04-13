import pygame as pg 
from pygame.locals import *
from item.item import Item
pg.init()

class Weapon(Item):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, width, height, color)
        self.name = 'weapon'
        self.tag = 'weapon'
        self.attack_power = 0

class Sword(Weapon):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, width, height, color)
        self.name = 'sword'
        self.attack_power = 10

    def equip(self, player):
        super().equip(player)
        player.image = pg.Surface((self.width, self.height))
        player.image.fill(self.color)
        player.rect = player.image.get_rect()
        player.rect.x = self.rect.x
        player.rect.y = self.rect.y