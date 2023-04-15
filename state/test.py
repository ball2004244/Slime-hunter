# create a sample pygame program 
import pygame as pg
from pygame.locals import *
from pause_screen import PauseScreen
pg.init()

# create a screen
screen = pg.display.set_mode((800, 600))

# create a clock
clock = pg.time.Clock()

# create a font
font = pg.font.SysFont('Arial', 30)

def function1():
    print('button1 clicked')

def function2():
    # quit the game
    pg.quit()
    exit()

pause_screen = PauseScreen(screen)
pause_screen.button1.setup_function(function1)
pause_screen.button2.setup_function(function2)
while True:
    # set the fps
    clock.tick(60)

    # clear the screen
    screen.fill((0, 0, 0))


    pause_screen.draw()

    # check mouse click


    # get the event
    for event in pg.event.get():
        # check mouse click
        if event.type == MOUSEBUTTONDOWN:
            mouse_pos = pg.mouse.get_pos()
            if pause_screen.button1.check_click(mouse_pos):
                pause_screen.button1.activate()
            if pause_screen.button2.check_click(mouse_pos):
                pause_screen.button2.activate()
        if event.type == QUIT:
            pg.quit()
            exit()


    # update the screen
    pg.display.update()