import pygame as pg
from setup import COLOR, SCREEN
from control import Control
from character.player import Player, StatusBar, ToolBar
from character.enemy import Slime
from item.food import Apple
from item.weapon import Sword
from item.armor import LeatherArmor
from inventory import Inventory, InventoryUI

player = Player(100, 100, 70, 70, COLOR['green'])
slime1 = Slime(200, 200, 80, 80, COLOR['gray'])
apple = Apple(300, 300, 30, 30, COLOR['red'])
apple2 = Apple(400, 400, 30, 30, COLOR['red'])
sword = Sword(500, 500, 30, 30, COLOR['blue'])
leather_armor = LeatherArmor(600, 600, 60, 60, COLOR['brown'])

inventory = Inventory(10)
control = Control(player, inventory)
status_bar = StatusBar(30, 30, 200, 50, COLOR['black'])
tool_bar = ToolBar(SCREEN.get_width() / 2 - 200, SCREEN.get_height() - 60, 400, 50, COLOR['black'])

item_list = [apple, apple2, sword, leather_armor]
enemy_list = [slime1]

# create pygame sprite groups
item_group = pg.sprite.Group()
enemy_group = pg.sprite.Group()
player_group = pg.sprite.Group()

player_group.add(player)
# loop through the item list and add them to the item group
for item in item_list:
    item_group.add(item)

# loop through the enemy list and add them to the enemy group
for enemy in enemy_list:
    enemy_group.add(enemy)

def show_hp(screen):
    # show hp on top of the slime, color: red
    slime1.show_hp(screen)