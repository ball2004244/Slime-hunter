import pygame as pg 
from pygame.locals import *

pg.init()

class Gameplay:
    def __init__(self, player_group, enemy_group):
        self.player_group = player_group
        self.enemy_group = enemy_group

    def set_inventory(self, inventory):
        self.inventory = inventory
    
    def set_hotbar(self, hotbar):
        self.hotbar = hotbar

    def update(self):
        if self.check_collision(self.player_group, self.enemy_group):
            player, enemy = self.check_collision(self.player_group, self.enemy_group)
            # if player and player.attack_state:
            #     player.attack(enemy, self.hotbar.current_item(), self.inventory)

            if enemy and enemy.attack_state:
                enemy.attack(player)


    def check_collision(self, group1, group2):
        # check using groupcollide
        # if collide, call the collide function of the sprite
        collide_list = pg.sprite.groupcollide(group1, group2, False, False)
        if collide_list:
            instance1 = list(collide_list.keys())[0]
            instance2 = collide_list[instance1][0]
            return instance1, instance2
        
        return None, None