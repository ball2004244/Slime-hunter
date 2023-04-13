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
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, width, height, color)
        self.name = 'leather_armor'
        self.defense = 10
        self.color = 'light_brown'

        self.image = pg.image.load('asset/image/armor_01a.png')
        self.image = pg.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        
    def equip(self, player):
        super().equip(player)
        player.image = pg.Surface((self.width, self.height))
        player.image.fill(self.color)
        player.rect = player.image.get_rect()
        player.rect.x = self.rect.x
        player.rect.y = self.rect.y