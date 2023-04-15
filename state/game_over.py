import pygame as pg
from state.pause_screen import PauseScreen

restart_image = pg.image.load('asset/image/restart_button.png')
class GameOver(PauseScreen):
    def __init__(self, screen):
        super().__init__(screen)

    def setup_buttons(self, button1, button2):
        super().setup_buttons(button1, button2)
                
        self.button1.setup_image(restart_image)
