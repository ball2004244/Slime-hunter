import pygame as pg
from state.pause_screen import PauseScreen

restart_image = pg.image.load('asset/image/restart_button.png')
class GameOver(PauseScreen):
    def __init__(self, screen):
        super().__init__(screen)
        self.score = 0

    def setup_buttons(self, button1, button2):
        super().setup_buttons(button1, button2)
                
        self.button1.setup_image(restart_image)

    def display_score(self):
        font = pg.font.SysFont('comicsans', 50)
        text = font.render(f'Score: {self.score}', 1, (255, 255, 255))
        self.screen.blit(text, (self.screen.get_width() / 2 - text.get_width() / 2, self.screen.get_height() / 2 - text.get_height() / 2 - 50))

    def draw(self):
        super().draw()
        self.display_score()