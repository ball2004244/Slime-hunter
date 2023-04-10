import pygame as pg
from setup import COLOR, SCREEN
from control import Control
from player import Player, StatusBar
""" from character.enemy import Slime
from item.food import Apple
from item.weapon import Sword
from item.armor import LeatherArmor
from item.tool import WoodenPickaxe
""" 
from inventory import Inventory, InventoryUI, HotBar 
"""
from block.block import WoodBlock, StoneBlock
 """
from camera import Camera
from map.map import Map

# create a map
# This is the dummy map from camera.py
# from camera import Map
# gamemap = Map(0, 0, MAP_WIDTH, MAP_HEIGHT)

# This is the real map from map/map.py
gamemap = Map(r'map/Slime hunter graphics/map.tmx')

""" # create enemies
slime1 = Slime(200, 200, 80, 80)


# create pickable items
apple = Apple(300, 300, 30, 30, COLOR['red'])
apple2 = Apple(400, 400, 30, 30, COLOR['red'])
sword = Sword(500, 500, 30, 30, COLOR['blue'])
leather_armor = LeatherArmor(600, 600, 60, 60, COLOR['light_brown'])
wooden_pickaxe = WoodenPickaxe(700, 700, 30, 30, COLOR['purple'])


# create blocks
wood_block = WoodBlock(100, 650, 50, 50, COLOR['brown'])
stone_block = StoneBlock(200, 650, 50, 50, COLOR['gray']) """


# define player
player = Player(400, 400, 70, 70, COLOR['green'])
inventory = Inventory(10)
status_bar = StatusBar(30, 30, 200, 50, COLOR['black'])
hotbar = HotBar(SCREEN.get_width() / 2 - 200, SCREEN.get_height() - 60, 400, 50, COLOR['black'])

""" # create lists
item_list = [apple, apple2, sword, leather_armor, wooden_pickaxe]
enemy_list = [slime1]
block_list = [wood_block, stone_block] """

# create pygame sprite groups
item_group = pg.sprite.Group()
enemy_group = pg.sprite.Group()
player_group = pg.sprite.Group()
block_group = pg.sprite.Group()

# add sprites to groups
player_group.add(player)

""" for item in item_list:
    item_group.add(item)

for enemy in enemy_list:
    enemy_group.add(enemy)

for block in block_list:
    block_group.add(block)

def show_hp(screen):
    # show hp on top of the slime, color: red
    slime1.show_hp(screen) """

# define camera
camera = Camera(player, SCREEN.get_width(), SCREEN.get_height(), gamemap.width, gamemap.height)
control = Control(player, inventory, hotbar, camera)