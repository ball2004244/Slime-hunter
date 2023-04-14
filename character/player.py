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
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.setup_equipment()
        self.setup_status()
        self.setup_transition()

        # direction: ['up', 'down', 'left', 'right']
        self.direction = 'right'
        self.pickup_state = True
        self.run_state = False
        self.moving = True
        self.alive = True

        self.attack_timer = pg.time.get_ticks()

    def setup_status(self):
        self.max_hp = 100
        self.hp = self.max_hp
        self.mp = 100
        self.attack_power = 10
        self.defense = 10
        self.default_speed = 3
        self.speed = self.default_speed

        print(self.get_status())

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
        if not self.alive:
            return

        if self.run_state == True:
            self.speed = self.default_speed * 2
        else:
            self.speed = self.default_speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def attack(self, enemy, weapon, inventory):
        current_time = pg.time.get_ticks()
        if current_time - self.attack_timer < 500:
            return

        # print('Attack!', enemy)
        weapon_attack_power = 0
        if weapon:
            if weapon.tag == 'weapon':
                weapon_attack_power = weapon.attack_power

        enemy.get_damage(self.attack_power + weapon_attack_power, inventory)
        self.attack_timer = current_time

    def pickup(self, inventory, item):
        if self.pickup_state == False:
            return

        if self.rect.colliderect(item.rect):
            inventory.add_item(item)

    def get_damage(self, damage):
        if not self.alive:
            return

        if damage > self.defense:
            self.hp -= (damage - self.defense)

        if self.hp <= 0:
            self.die()

    def equip(self, item):
        if item.tag == 'armor':
            self.armor = item
        elif item.tag == 'helmet':
            self.helmet = item
        elif item.tag == 'boots':
            self.boots = item

    def break_block(self, tool, block, inventory):
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

        block.get_broken(tool, inventory)

    def die(self):
        print('You are dead!')
        self.alive = False
        self.speed = 0

    def get_save_data(self):
        status = self.get_status()

        save_dict = {'x': self.rect.x, 'y': self.rect.y,
                     'width': self.width, 'height': self.height, 'status': status}

        return save_dict

    def load_data(self, save_data):
        self.rect.x = save_data['x']
        self.rect.y = save_data['y']
        self.width = save_data['width']
        self.height = save_data['height']

        self.status = save_data['status']
        self.load_status(self.status)

    def get_status(self):
        self.status = {'max_hp': self.max_hp, 'hp': self.hp, 'mp': self.mp,
                       'attack_power': self.attack_power, 'defense': self.defense, 'speed': self.speed}
        return self.status
    
    def get_pos(self):
        return self.rect.x, self.rect.y
    
    def load_status(self, status):
        self.max_hp = status['max_hp']
        self.hp = status['hp']
        self.mp = status['mp']
        self.attack_power = status['attack_power']
        self.defense = status['defense']
        self.speed = status['speed']


class StatusBar(pg.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.image = pg.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def show_hp(self, screen, player):
        # show hp on top of the slime, color: red
        # draw a rect similar to enemy hp bar
        pg.draw.rect(screen, COLOR['red'], (self.rect.x, self.rect.y,
                     player.hp / player.max_hp * self.width, 10))

    def show_mp(self, screen, player):
        # show hp on top of the slime, color: red
        pg.draw.rect(screen, COLOR['blue'], (self.rect.x,
                     self.rect.y + 20, player.mp * 2, 10))

    def show_status(self, screen, player):
        self.show_hp(screen, player)
        self.show_mp(screen, player)

    def get_status(self):
        pass

    def get_pos(self):
        pass


if __name__ == '__main__':
    print('This is a module for player class. Please run main.py to start the game.')
