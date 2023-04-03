import pygame as pg
from pygame.locals import *

pg.init()

class Apple(pg.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.image = pg.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.pickup_state = True

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def pickup(self):
        self.pickup_state = False
        # self.kill()
    
