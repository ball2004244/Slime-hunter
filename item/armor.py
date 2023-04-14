import pygame as pg 
from pygame.locals import *
from item.item import Item
pg.init()

class Armor(Item):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, width, height, color)
        self.name = 'armor'
        self.tag = 'armor'
        self.defense = 0


class LeatherArmor(Armor):
    def __init__(self, x, y, width, height, color=(255, 255, 255)):
        super().__init__(x, y, width, height, color)
        self.name = 'leather_armor'
        self.defense = 10
        self.color = color

        self.image = pg.image.load('asset/image/armor_01a.png')
        self.image = pg.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def equip(self, player):
        super().equip(player)
        self.rect.x = player.rect.x
        self.rect.y = player.rect.y