import pygame as pg
from pygame.locals import *
import configparser

pg.init()

# get data from config.cfg
config = configparser.ConfigParser()
config.read('config.cfg')
screen_width = config.getint('window', 'WIDTH')
screen_height = config.getint('window', 'HEIGHT')
screen_title = config.get('window', 'TITLE')

COLOR = {}
for color_name in config.options('color'):
    COLOR[color_name] = tuple(map(int, config.get('color', color_name).split(',')))

def screen_setup():
    global Screen
    Screen = pg.display.set_mode((screen_width, screen_height))
    pg.display.set_caption(screen_title)
    # set screen to white 
    Screen.fill(COLOR['white'])
