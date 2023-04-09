import pygame as pg
from pygame.locals import *
from setup import SCREEN, COLOR
pg.init()

# create Enemy abstract class as a sprite
class Enemy(pg.sprite.Sprite):
    def __init__(self, x, y, width, height, color, resource=None):
        super().__init__()
        self.image = pg.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height

        self.resource = resource

        self.setup_status()

        self.tag = 'enemy'
        self.name = 'enemy'

        self.attack_state = True


    def setup_status(self):
        self.max_hp = 10
        self.hp = self.max_hp
        self.mp = 0
        self.attack_power = 1
        self.defense = 5
        self.default_speed = 3

    def attack(self, player):
        if self.attack_state:
            player.get_damage(self.attack_power)
            self.attack_state = False
        
    
    def get_damage(self, damage, inventory):
        if damage > self.defense:
            self.hp -= (damage - self.defense)
            if self.hp <= 0:
                self.die(inventory)

    def show_hp(self, screen):
        # show hp on top of the slime, color: red
        # the bar only have width = self.width when hp = self.max_hp
        # => hp/max_hp = width/max_width
        # => width = hp/max_hp * max_width
        pg.draw.rect(screen, COLOR['red'], (self.rect.x, self.rect.y - 10, self.hp/self.max_hp * self.width, 5))

    def drop(self, inventory):
        inventory.add_item(self.resource)

    def die(self, inventory):
        self.drop(inventory)
        self.kill()

    
# create Slime class as a sprite
class Slime(Enemy):
    def __init__(self, x, y, width, height, color, resource):
        super().__init__(x, y, width, height, color, resource)

        self.setup_status()
        self.tag = 'enemy'
        self.name = 'slime'

    def setup_status(self):
        self.max_hp = 10
        self.hp = self.max_hp
        self.mp = 0
        self.attack_power = 50
        self.defense = 5
        self.default_speed = 3
