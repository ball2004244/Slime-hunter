import pygame as pg 
from pygame.locals import *
import random
import sys
pg.init()

class Gameplay:
    def __init__(self, SCREEN):
        self.screen = SCREEN

        self.timer = pg.time.get_ticks()
        self.spawn_timer = pg.time.get_ticks()
    

    def resume(self):
        self.control.pause_state = False

    def restart(self):
        if self.player.alive:
            return
        
        self.player.alive = True

        # reset player's position
        self.player.rect.x = 700
        self.player.rect.y = 500

        # reset player's hp
        self.player.hp = self.player.max_hp


        # reset player's inventory
        self.inventory.empty()
        self.hotbar.empty()

        # reset items and enemies
        self.item_group.empty()
        self.enemy_group.empty()

        # spawn new items 
        self.create_item(self.item_dict)
        # reset player's score
        self.score = 0

    def game_exit(self):
        self.save_game()
        pg.quit()
        sys.exit()

    def setup_pause_screen(self, pause_screen):
        self.pause_screen = pause_screen

        self.pause_screen.button1.setup_function(self.resume)
        self.pause_screen.button2.setup_function(self.game_exit)

    def setup_game_over(self, game_over_screen):
        self.game_over_screen = game_over_screen

        self.game_over_screen.button1.setup_function(self.restart)
        self.game_over_screen.button2.setup_function(self.game_exit)

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
        if current - self.timer < 10000:
            return
        
        self.timer = current
        self.save_game()
        # print('Saving')

    def setup_enemy(self, Enemy, color, coin):
        self.Enemy = Enemy
        self.color = color
        self.coin = coin

    def create_enemy(self, Enemy, color, coin):
        num_enemy = random.randint(5, 10)

        # generate a list of x,y in [100, 900] and normal distribution
        # there are 2 lists will have the range of num_enemy / 3
        # if either list surpass that length, empty the list and restart the random
        temp_x = []
        temp_y = []
        for i in range(num_enemy):
            # generate a random position at least 100 pixels away from the player
            dist = 0
            while dist < 100:
                x = random.randint(100, 900)
                y = random.randint(100, 900)
                dist = ((x - self.player.rect.x) ** 2 + (y - self.player.rect.y) ** 2) ** 0.5

            # if the current pos is too close to the previous pos, restart the random
            while len(temp_x) > 0 and abs(x - temp_x[-1]) < 100:
                x = random.randint(100, 900)
                dist = ((x - self.player.rect.x) ** 2 + (y - self.player.rect.y) ** 2) ** 0.5
            while len(temp_y) > 0 and abs(y - temp_y[-1]) < 100:
                y = random.randint(100, 900)
                dist = ((x - self.player.rect.x) ** 2 + (y - self.player.rect.y) ** 2) ** 0.5

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

    def enemy_movement(self):
        # enemy attack
        for enemy in self.enemy_group:
            enemy.move_towards_player(self.player)

    def spawn_enemy(self, Enemy, color, coin):
        # spawn every 10 seconds
        current = pg.time.get_ticks()
        if current - self.spawn_timer < 5000:
            return
        
        self.spawn_timer = current
        self.create_enemy(Enemy, color, coin)

    def setup_item(self, item_dict):
        self.item_dict = item_dict

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
        
    def get_movable_objects(self):
        # store all of them in a lists
        movable_objects = []
        movable_objects.extend(self.player_group.sprites())
        movable_objects.extend(self.enemy_group.sprites())
        movable_objects.extend(self.item_group.sprites())
        movable_objects.extend(self.block_group.sprites())

        return movable_objects

    def quit(self):
        pg.quit()
        sys.exit()

    def game_loop(self):
        # process the user keyboard + mouse input
        self.control.event_loop(self.player_group, self.item_group, self.enemy_group, self.block_group, self.pause_screen, self.game_over_screen) 
        
        self.fps_clock.display_fps(self.screen)
        pg.display.update()

        if self.control.is_paused():
            # reset the timer
            current = pg.time.get_ticks()
            self.timer = current
            self.spawn_timer = current
            return
        
        # fill screen with white
        self.screen.fill((255, 255, 255))

        self.gamemap.render(self.screen)
    
        self.item_group.draw(self.screen)
        self.player_group.draw(self.screen)
        self.enemy_group.draw(self.screen)
        # self.block_group.draw(self.screen)

        # show status
        self.show_status()
        self.hotbar.draw(self.screen)

        # player's hitbox
        self.player.update_hitbox()

        # game mechanics
        self.spawn_enemy(self.Enemy, self.color, self.coin)
        self.enemy_movement()

        # update camera
        self.camera.update(self.gamemap, self.get_movable_objects())
        

        # auto save every 10 seconds
        # self.auto_save()

        # immediately save
        # self.save_game() 
