import pygame as pg
from pygame.locals import *

pg.init()

class Slime(pg.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.image = pg.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move(self, x, y):
        self.rect.x += x
        self.rect.y += y

    def draw(self, screen):
        screen.blit(self.image, self.rect)