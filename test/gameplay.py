import pygame as pg 
from pygame.locals import *


pg.init()

class Gameplay:
    def __init__(self, SCREEN):
        self.screen = SCREEN

    def setup_gamemap(self, gamemap):
        self.gamemap = gamemap

    def setup_player_group(self, player):
        self.player = player

    def setup_show_hp(self, hp, mp):
        self.hp = hp
        self.mp = mp

    def setup_hotbar(self, hotbar):
        self.hotbar = hotbar

    def setup_item_group(self, weapon, tool, food, armor, item):
        self.weapon = weapon
        self.tool = tool
        self.food = food
        self.armor = armor
        self.item = item


    def setup_enemy_group(self, enemy):
        self.enemy = enemy

    def setup_inventory(self, inventory):
        self.inventory = inventory

    def setup_control(self, control):
        self.control = control

    def setup_camera(self, camera):
        self.camera = camera

    def save_game(self, save_game):
        self.save_game = save_game

    def fps_clock(self, fps_clock):
        self.fps_clock = fps_clock
    

    """ def setup_block_group() """

    def game_loop():
        # fill screen with white
        self.screen.fill(COLOR['white'])

        self.gamemap.render(self.screen)

        self.player_group.draw(self.screen)
        self.enemy_group.draw(self.screen)
        self.item_group.draw(self.screen)
        self.block_group.draw(self.screen)

        # show status

        self.show_hp(self.screen)
        self.hotbar(self.screen)
        # slime1.random_movement(movement, camera)

        # process the user keyboard + mouse input
        self.control.event_loop(player_group, item_group, enemy_group)            

        self.camera.update(gamemap)
        
        self.save_game()
        
        fps_clock.display_fps(self.screen)
        pg.display.update()