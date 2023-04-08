import pygame as pg
from pygame.locals import *
pg.init()

# create an abstract class named block as a sprite
class Block(pg.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
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

    # the player can interact with the block
    # then he will get resources inside the inventory
    def gather(self, inventory):
        inventory.add_item(self)

    # the user need to have a tool to break the block
    # the tool's mining level must be higher than the block's mining level
    def get_broken(self, tool):
        if tool.mining_power >= self.mining_level:
            self.hp -= 1
            tool.durability -= 1
            print(f'{self.name}: {self.hp}')
            if self.hp <= 0:
                self.kill()
        else:
            print('You need a better tool to break this block.')

class WoodBlock(Block):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, width, height, color)
        self.name = 'wood'
        self.tag = 'wood'
        self.mining_level = 1

class StoneBlock(Block):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, width, height, color)
        self.name = 'stone'
        self.tag = 'stone'
        self.mining_level = 2
