import pygame as pg 
from pygame.locals import *
import random
pg.init()

class Gameplay:
    def __init__(self, SCREEN):
        self.screen = SCREEN
        self.timer = pg.time.get_ticks()
    
    def setup_map(self, gamemap):
        self.gamemap = gamemap

    def setup_status(self, status_bar):
        self.status_bar = status_bar
    
    def show_status(self):
        self.status_bar.show_status(self.screen, self.player)
        for enemy in self.enemy_group:
            enemy.show_hp(self.screen)

    def setup_entity_group(self, player_group, item_group, enemy_group, block_group):
        self.player_group = player_group
        self.item_group = item_group
        self.enemy_group = enemy_group
        self.block_group = block_group

        self.player = self.player_group.sprites()[0]
    def setup_inventory(self, inventory, hotbar):
        self.inventory = inventory
        self.hotbar = hotbar

    def setup_utilities(self, camera, control, save_game, fps_clock):
        self.camera = camera
        self.control = control
        self.save_game = save_game
        self.fps_clock = fps_clock

    def auto_save(self):
        # set a timer to save the game
        current = pg.time.get_ticks()
        if current - self.timer >= 10000:
            self.timer = current
            self.save_game()
            # print('Saving')

    def create_enemy(self, Enemy, color, coin):
        num_slime = random.randint(5, 10)
        for i in range(num_slime):
            x = random.randint(100, 1000)
            y = random.randint(100, 900)
            enemy = Enemy(x, y, 50, 50, color, coin)
            self.enemy_group.add(enemy)        

    # rewrite the create_enemy with random distribution
    def create_enemy(self, Enemy, color, coin):
        num_enemy = random.randint(5, 10)

        # generate a list of x,y in [100, 900] and normal distribution
        # there are 2 lists will have the range of num_enemy / 3
        # if either list surpass that length, empty the list and restart the random
        temp_x = []
        temp_y = []
        for i in range(num_enemy):
            x = random.randint(100, 900)
            y = random.randint(100, 900)

            # if the current pos is too close to the previous pos, restart the random
            while len(temp_x) > 0 and abs(x - temp_x[-1]) < 100:
                x = random.randint(100, 900)
            while len(temp_y) > 0 and abs(y - temp_y[-1]) < 100:
                y = random.randint(100, 900)

            temp_x.append(x)
            temp_y.append(y)

            # reset the list if it is too long
            if len(temp_x) > num_enemy / 3:
                temp_x = []
            if len(temp_y) > num_enemy / 3:
                temp_y = []

            # create enemy
            enemy = Enemy(x, y, 50, 50, color, coin)
            self.enemy_group.add(enemy)


    def create_item(self, item_dict):
        num_item = random.randint(5, 10)
        
        # generate a list of x,y in [100, 900] and normal distribution
        # there are 2 lists will have the range of num_item / 3
        # if either list surpass that length, empty the list and restart the random
        temp_x = []
        temp_y = []
        for i in range(num_item):
            x = random.randint(100, 900)
            y = random.randint(100, 900)

            # if the current pos is too close to the previous pos, restart the random
            while len(temp_x) > 0 and abs(x - temp_x[-1]) < 100:
                x = random.randint(100, 900)
            while len(temp_y) > 0 and abs(y - temp_y[-1]) < 100:
                y = random.randint(100, 900)
            temp_x.append(x)
            temp_y.append(y)

            # reset the list if it is too long
            if len(temp_x) > num_item / 3:
                temp_x = []
            if len(temp_y) > num_item / 3:
                temp_y = []

            # create item
            item_choice = random.choice(list(item_dict.values()))
            item = item_choice(x, y, 50, 50)
            self.item_group.add(item)
        
    def game_loop(self):
        # fill screen with white
        self.screen.fill((255, 255, 255))

        self.gamemap.render(self.screen)
    
        self.player_group.draw(self.screen)
        self.enemy_group.draw(self.screen)
        self.item_group.draw(self.screen)
        # self.block_group.draw(self.screen)

        # # show status
        self.show_status()
        self.hotbar.draw(self.screen)
        # # slime1.random_movement(movement, camera)

        # # process the user keyboard + mouse input
        self.control.event_loop(self.player_group, self.item_group, self.enemy_group, self.block_group)          

        self.camera.update(self.gamemap)
        
        # auto save every 10 seconds
        self.auto_save()

        # immediately save
        # self.save_game() 
        
        self.fps_clock.display_fps(self.screen)
        pg.display.update()
