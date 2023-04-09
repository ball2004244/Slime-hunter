import pygame as pg
from pygame.locals import *
pg.init()

# create an abstract class named block as a sprite
class Block(pg.sprite.Sprite):
    def __init__(self, x, y, width, height, color, resource=None):
        super().__init__()
        self.image = pg.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height

        self.name = 'block'
        self.tag = 'block'

        # the number of times the block can be broken
        self.hp = 10

        self.mining_level = 0
        self.resource = resource

    def gather(self, inventory):
        inventory.add_item(self.resource)

    # the user need to have a tool to break the block
    # the tool's mining level must be higher than the block's mining level
    def get_broken(self, tool, inventory):
        if tool.mining_power >= self.mining_level:
            self.hp -= 1
            tool.durability -= 1
            self.gather(inventory)
            print(f'{self.name}: {self.hp}')
            if self.hp <= 0:
                self.kill()
        else:
            print('You need a better tool to break this block.')

class WoodBlock(Block):
    def __init__(self, x, y, width, height, color, resource):
        super().__init__(x, y, width, height, color, resource)
        self.name = 'wood_block'
        self.tag = 'wood_block'
        self.mining_level = 1

class StoneBlock(Block):
    def __init__(self, x, y, width, height, color, resource):
        super().__init__(x, y, width, height, color, resource)
        self.name = 'stone_block'
        self.tag = 'stone_block'
        self.mining_level = 2
