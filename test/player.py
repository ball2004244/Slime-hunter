import pygame as pg 
from pygame.locals import *
from setup import SCREEN, COLOR

pg.init()

# create a character class as a sprite
class Player(pg.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.image = pg.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        

        self.setup_equipment()
        self.setup_status()
        self.setup_transition()

        # direction: ['up', 'down', 'left', 'right']
        self.direction = 'right'
        self.attack_state = True
        self.pickup_state = True
        self.run_state = False


    def setup_status(self):
        self.hp = 100
        self.mp = 100
        self.attack_power = 10
        self.defense = 10
        self.default_speed = 3
        self.speed = self.default_speed


    def setup_equipment(self):
        self.armor = None
        self.helmet = None
        self.boots = None

        # armor, helmet, boots
        self.equipment_list = [self.armor, self.helmet, self.boots]

    def setup_transition(self):
        self.top_transition = False
        self.bottom_transition = False
        self.left_transition = False
        self.right_transition = False

        self.speed_top = self.speed
        self.speed_bottom = self.speed
        self.speed_left = self.speed
        self.speed_right = self.speed


    # create 4 functions to move the character
    def move_up(self): 
        if self.top_transition:
            self.speed_top = 0
            return
        
        self.speed_top = self.speed

        if self.rect.y > 0:
            self.rect.y -= self.speed_top
            self.direction = 'up'

    def move_down(self):
        if self.bottom_transition:
            self.speed_bottom = 0
            return
        
        self.speed_bottom = self.speed

        if self.rect.y < SCREEN.get_height() - self.rect.height:
            self.rect.y += self.speed_bottom
            self.direction = 'down'

    def move_left(self):
        if self.left_transition:
            self.speed_left = 0
            return

        self.speed_left = self.speed

        if self.rect.x > 0:
            self.rect.x -= self.speed_left
            self.direction = 'left'

    def move_right(self):
        if self.right_transition:
            self.speed_right = 0
            return
        
        self.speed_right = self.speed
        
        if self.rect.x < SCREEN.get_width() - self.rect.width:
            self.rect.x += self.speed_right
            self.direction = 'right'

    def run(self):
        if self.run_state == True:
            self.speed = self.default_speed * 2
        else:
            self.speed = self.default_speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def attack(self, enemy, weapon):
        if self.attack_state == False:
            return

        if self.rect.colliderect(enemy.rect):
            # print('Attack!', enemy)
            weapon_attack_power = 0
            if weapon:
                if weapon.tag == 'weapon':
                    weapon_attack_power = weapon.attack_power
            enemy.get_damage(self.attack_power + weapon_attack_power)


    def pickup(self, hotbar, inventory, item):
        if self.pickup_state == False:
            return

        if self.rect.colliderect(item.rect):
            inventory.add_item(item, hotbar)

    def get_damage(self, damage):
        if self.hp <= 0:
            print('You are dead!')
            return
        
        if damage > self.defense:
            self.hp -= (damage - self.defense)

    def equip(self, item):
        if item.tag == 'armor':
            self.armor = item
        elif item.tag == 'helmet':
            self.helmet = item
        elif item.tag == 'boots':
            self.boots = item

    def break_block(self, tool, block):
        # This means the player is not holding any tool
        if tool == None:
            print('You need a tool to break the block.')
            return
        
        # check if the tool is a pickaxe
        if tool.tag != 'tool':
            print('You need a pickaxe to break the block.')
            return
        
        # check if there is a pickage str in the name 
        if 'pickaxe' not in tool.name:
            print('You need a pickaxe to break the block.')
            return
        
        block.get_broken(tool)


class StatusBar(pg.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.image = pg.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def show_hp(self, screen, player):
        # show hp on top of the slime, color: red
        pg.draw.rect(screen, COLOR['red'], (self.rect.x, self.rect.y, player.hp * 2, 10))

    def show_mp(self, screen, player):
        # show hp on top of the slime, color: red
        pg.draw.rect(screen, COLOR['blue'], (self.rect.x, self.rect.y + 20, player.mp * 2, 10))
    
    def show_status(self, screen, player):
        self.show_hp(screen, player)
        self.show_mp(screen, player)

if __name__ == '__main__':
    print('This is a module for player class. Please run main.py to start the game.')




