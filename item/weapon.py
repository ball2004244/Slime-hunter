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
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, width, height, color)
        self.name = 'sword'
        self.attack_power = 10
        self.color = 'blue'

    def equip(self, player):
        super().equip(player)
        player.image = pg.Surface((self.width, self.height))
        player.image.fill(self.color)
        player.rect = player.image.get_rect()
        player.rect.x = self.rect.x
        player.rect.y = self.rect.y