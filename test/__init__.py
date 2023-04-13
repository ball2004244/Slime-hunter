import pygame as pg
from setup import COLOR, SCREEN
from character.player import Player, StatusBar
from character.enemy import Slime
from block.block import WoodBlock, StoneBlock
from item.food import Apple
from item.weapon import Sword
from item.armor import LeatherArmor
from item.tool import WoodenPickaxe
from item.resource import Wood, Stone, Coin
from utilities.control import Control
from utilities.camera import Camera
from utilities.inventory import Inventory, HotBar
from utilities.helper import movement
from save.save import save_object, load_object, reset_file, save_to_file, load_from_file
from map.map import Map
# from state.gameplay import Gameplay

# create pickable items
apple = Apple(300, 300, 30, 30, COLOR['red'])
apple2 = Apple(400, 400, 30, 30, COLOR['red'])
sword = Sword(500, 500, 30, 30, COLOR['blue'])
leather_armor = LeatherArmor(600, 600, 60, 60, COLOR['light_brown'])
wooden_pickaxe = WoodenPickaxe(700, 700, 30, 30, COLOR['purple'])

# define items
wood = Wood(0, 0, 30, 30)
stone = Stone(0, 0, 30, 30)
coin = Coin(0, 0, 30, 30)

# create blocks
wood_block = WoodBlock(100, 650, 50, 50, COLOR['brown'], wood)
stone_block = StoneBlock(200, 650, 50, 50, COLOR['gray'], stone)

# create enemies
slime1 = Slime(100, 100, 50, 50, COLOR['black'], coin)


# define player
player = Player(700, 500, 70, 70, COLOR['green'])
hotbar = HotBar(SCREEN.get_width() / 2 - 200,
                SCREEN.get_height() - 60, 400, 50, COLOR['black'])
inventory = Inventory(10, hotbar)
status_bar = StatusBar(30, 30, 200, 50, COLOR['black'])

control = Control(player, inventory, hotbar)

# create lists
item_list = [apple, apple2, sword, leather_armor, wooden_pickaxe]
enemy_list = [slime1]
block_list = [wood_block, stone_block]

# create pygame sprite groups
item_group = pg.sprite.Group()
enemy_group = pg.sprite.Group()
player_group = pg.sprite.Group()
block_group = pg.sprite.Group()

# add sprites to groups
player_group.add(player)

for item in item_list:
    item_group.add(item)

for enemy in enemy_list:
    enemy_group.add(enemy)

for block in block_list:
    block_group.add(block)

# show hp on top of the enemies


def show_hp(screen):
    status_bar.show_status(SCREEN, player)
    slime1.show_hp(screen)


# create map
gamemap = Map(r'map/Slime hunter graphics/map.tmx')
# create a game camera
camera = Camera(player, SCREEN.get_width(), SCREEN.get_height(), gamemap.width, gamemap.height)

def save_game():
    # reset save file
    reset_file('save/player.pkl')
    for obj in player_group:
        save_object(obj, 'save/player.pkl')

    item_list = []
    for obj in item_group:
        saved_data = obj.get_save_data()
        item_list.append(saved_data)

    reset_file('save/item.pkl')
    save_to_file('save/item.pkl', item_list)

def load_game():
    # empty each group first 
    player_group.empty()
    load_object(player, 'save/player.pkl')
    player_group.add(player)

    item_group.empty()
    item_data_list = load_from_file('save/item.pkl')
    for data in item_data_list:
        item = Item(100, 100, 30, 30, COLOR['red'])
        item.load_save_data(data)
        item_group.add(item)

# create gpytameplay state
# gameplay = Gameplay(player_group, enemy_group)
# gameplay.set_inventory(inventory)
# gameplay.set_hotbar(hotbar)