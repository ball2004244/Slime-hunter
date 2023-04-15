import pygame as pg
from pygame.locals import *

pg.init()

class PauseScreen:
    def __init__(self, screen):
        self.screen = screen
        self.width, self.height = screen.get_size()
        # setup title
        self.title = 'Slime Hunter'
        self.title_font = pg.font.SysFont('Arial', 50)
        self.title_text = self.title_font.render(self.title, True, (255, 255, 255))
        self.title_rect = self.title_text.get_rect()
        self.title_rect.center = (self.width / 2, self.height / 2 - 200)

        # setup background image
        # self.background = pg.image.load('assets/images/backgrounds/pause_screen.png')
        # self.background_rect = self.background.get_rect()
        # self.background_rect.center = (400, 300)
        # no background image so we use a mock background by filling the screen with black
        self.background = pg.Surface((self.width, self.height))
        self.background.fill((0, 0, 0))
        self.background_rect = self.background.get_rect()

    def setup_buttons(self, button1, button2):
        self.button1 = button1
        self.button2 = button2

    def draw(self):
        self.screen.blit(self.background, self.background_rect)
        self.screen.blit(self.title_text, self.title_rect)
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

        # setup font
        self.font = pg.font.SysFont('Arial', 30)
        self.text = self.font.render(self.text, True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.x + self.width / 2, self.y + self.height / 2)

    def draw(self):
        pg.draw.rect(self.screen, (255, 255, 255), (self.x, self.y, self.width, self.height))
        self.screen.blit(self.text, self.text_rect)

    def check_click(self, mouse_pos):
        if self.x <= mouse_pos[0] <= self.x + self.width and self.y <= mouse_pos[1] <= self.y + self.height:
            return True
        return False
    
    def setup_function(self, function):
        self.function = function

    def activate(self):
        self.function()