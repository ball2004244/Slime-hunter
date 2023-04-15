import pygame as pg
from pygame.locals import *

pg.init()

title_image = pg.image.load('asset/image/title.png')
background = pg.image.load('asset/image/background.png')
button1_image = pg.image.load('asset/image/play_button.png')
button2_image = pg.image.load('asset/image/quit_button.png')

class PauseScreen:
    def __init__(self, screen):
        self.screen = screen
        self.width, self.height = screen.get_size()

        # setup title
        self.title_image = title_image
        self.title_image = pg.transform.scale(self.title_image, (self.width * 5 / 8, self.height / 8))

        self.title_rect = self.title_image.get_rect()
        self.title_rect.center = (self.width / 2, self.height / 4)

        # setup background image
        self.background = background
        self.background = pg.transform.scale(self.background, (self.width, self.height))

        self.background_rect = self.background.get_rect()
        self.background_rect.center = (self.width / 2, self.height / 2)
    

    def setup_buttons(self, button1, button2):
        self.button1 = button1
        self.button2 = button2

        self.button1.setup_image(button1_image)
        self.button2.setup_image(button2_image)

    def draw(self):
        self.screen.blit(self.background, self.background_rect)
        self.screen.blit(self.title_image, self.title_rect)
        self.button1.draw()
        self.button2.draw()
        
    def update(self):
        pass

class Button:
    def __init__(self, screen, text, x, y, width, height):
        self.screen = screen
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)

    def setup_image(self, image):
        self.image = image
        self.image = pg.transform.scale(self.image, (self.width, self.height))

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def check_click(self, mouse_pos):
        if self.x <= mouse_pos[0] <= self.x + self.width and self.y <= mouse_pos[1] <= self.y + self.height:
            return True
        return False
    
    def setup_function(self, function):
        self.function = function

    def activate(self):
        self.function()