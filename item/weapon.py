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
        self.color = (255, 255, 255)

    def get_save_data(self):
        data = super().get_save_data()
        data['tag'] = self.tag

        return data
    
    def load_data(self, save_data):
        super().load_data(save_data)
        self.tag = save_data['tag']


class Sword(Weapon):
    def __init__(self, x, y, width, height, color=(0, 0, 255)):
        super().__init__(x, y, width, height, color)
        self.name = 'sword'
        self.attack_power = 10
        self.color = 'blue'

        self.image = pg.image.load('asset/image/sword_01b.png')
        self.image = pg.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


    def equip(self, player):
        super().equip(player)
        self.rect.x = player.rect.x
        self.rect.y = player.rect.y