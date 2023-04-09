import pygame as pg
import configparser

# Initialize Pygame
pg.init()

# Read the configuration file
config = configparser.ConfigParser()
config.read('config.cfg')

# Get the window settings from the configuration file
window_config = config['window']
screen_width = window_config.getint('WIDTH')
screen_height = window_config.getint('HEIGHT')
screen_title = window_config.get('TITLE')

# Get the color settings from the configuration file
color_config = config['color']
COLOR = {color_name: tuple(map(int, color_rgb.split(',')))
         for color_name, color_rgb in color_config.items()}

# Get default FPS from the configuration file
fps_config = config['fps']
FPS = fps_config.getint('FPS')

#  Set up the window
SCREEN = pg.display.set_mode((screen_width, screen_height))

def window_setup():
    pg.display.set_caption(screen_title)

    """ icon = pg.image.load(r'asset/image/favicon.jpg')
    pg.display.set_icon(icon) """

class FPS_clock:
    def __init__(self):
        self.clock = pg.time.Clock()
        self.FPS = FPS

    def tick(self):
        self.clock.tick(self.FPS)

    def get_fps(self):
        return str(int(self.clock.get_fps()))

    def display_fps(self, screen):
        self.tick()
        fps = self.get_fps()
        fps_text = pg.font.SysFont('arial', 25).render(fps, 1, COLOR['blue'])
        screen.blit(fps_text, (screen_width - 50, 10))

if __name__ == '__main__':
    print(FPS)
