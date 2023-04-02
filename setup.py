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

#  Set up the window
Screen = pg.display.set_mode((screen_width, screen_height))

def screen_setup():
    pg.display.set_caption(screen_title)


if __name__ == '__main__':
    print(Screen.get_height())
