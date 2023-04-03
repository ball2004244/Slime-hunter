import pygame as pg 
from pygame.locals import *
from setup import SCREEN

pg.init()

# create a character class as a sprite
class Player(pg.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.image = pg.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.setup_status()

        # direction: ['up', 'down', 'left', 'right']
        self.direction = 'right'
        self.attack_state = False
        self.pickup_state = False

    def setup_status(self):
        self.hp = 100
        self.mp = 100
        self.attack_power = 10
        self.defense = 10
        self.speed = 3

    # create 4 functions to move the character
    def move_up(self): 
        if self.rect.y > 0:
            self.rect.y -= self.speed
            self.direction = 'up'

    def move_down(self):
        if self.rect.y < SCREEN.get_height() - self.rect.height:
            self.rect.y += self.speed
            self.direction = 'down'

    def move_left(self):
        if self.rect.x > 0:
            self.rect.x -= self.speed
            self.direction = 'left'

    def move_right(self):
        if self.rect.x < SCREEN.get_width() - self.rect.width:
            self.rect.x += self.speed
            self.direction = 'right'

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def attack(self, enemy):
        self.attack_state = True
        if self.rect.colliderect(enemy.rect):
            print('Attack!', enemy)

        # wait for 0.5 second
        self.attack_state = False

    def pickup(self, item):
        self.pickup_state = True

        if self.rect.colliderect(item.rect):
            print('Pick up!', item)

        # wait for 0.5 second
        self.pickup_state = False

if __name__ == '__main__':
    print('This is a module for player class. Please run main.py to start the game.')