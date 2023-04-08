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
        self.weapon = None
        self.armor = None

    # create 4 functions to move the character
    def move_up(self): 
        if self.rect.y > 0:
            self.rect.y -= self.speed
            self.direction = 'up'

    def move_down(self):
        if self.rect.y < SCREEN.get_height() - self.rect.height:
            self.rect.y += self.speed
            self.direction = 'down'

    def move_left(self):
        if self.rect.x > 0:
            self.rect.x -= self.speed
            self.direction = 'left'

    def move_right(self):
        if self.rect.x < SCREEN.get_width() - self.rect.width:
            self.rect.x += self.speed
            self.direction = 'right'

    def run(self):
        if self.run_state == True:
            self.speed = self.default_speed * 2
        else:
            self.speed = self.default_speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def attack(self, enemy):
        if self.attack_state == False:
            return

        if self.rect.colliderect(enemy.rect):
            # print('Attack!', enemy)

            enemy.get_damage(self.attack_power)


    def pickup(self, inventory, item):
        if self.pickup_state == False:
            return

        if self.rect.colliderect(item.rect):
            # add item to inventory
            if not inventory.add_item(item):
                return 
               
            self.equip(item)         

    def get_damage(self, damage):
        if self.hp <= 0:
            print('You are dead.')
            return
        
        if damage > self.defense:
            self.hp -= (damage - self.defense)

    def equip(self, item):
        if item.tag == 'weapon':
            self.weapon = item
            self.attack_power += item.attack_power
        elif item.tag == 'armor':
            self.armor = item
            self.defense += item.defense


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


class ToolBar(pg.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.image = pg.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        screen.blit(self.image, self.rect)


