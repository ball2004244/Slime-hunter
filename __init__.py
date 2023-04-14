import pygame as pg
from setup import COLOR, SCREEN, FPS_clock, window_setup
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
from save.save import save_object, load_object, reset_file, save_to_file, load_from_file
from map.map import Map
from state.gameplay import Gameplay

# set up windows
window_setup()
# create clock
fps_clock = FPS_clock()

'''# create pickable items
apple = Apple(300, 300, 30, 30, COLOR['red'])
apple2 = Apple(400, 400, 30, 30, COLOR['red'])
sword = Sword(500, 500, 30, 30, COLOR['blue'])
leather_armor = LeatherArmor(600, 600, 60, 60, COLOR['light_brown'])
wooden_pickaxe = WoodenPickaxe(700, 700, 30, 30, COLOR['purple'])

# define items
wood = Wood(0, 0, 30, 30)
stone = Stone(0, 0, 30, 30)

# create blocks
wood_block = WoodBlock(100, 650, 50, 50, COLOR['brown'], wood)
stone_block = StoneBlock(200, 650, 50, 50, COLOR['gray'], stone)

# create enemies
slime1 = Slime(100, 100, 50, 50, COLOR['black'], coin)
'''


coin = Coin(0, 0, 40, 40, COLOR['yellow'])

# define player
player = Player(700, 500, 70, 70, COLOR['green'])
hotbar = HotBar(SCREEN.get_width() / 2 - 200,
                SCREEN.get_height() - 60, 400, 50, COLOR['black'])
inventory = Inventory(10, hotbar)
status_bar = StatusBar(30, 30, 200, 50, COLOR['black'])

control = Control(player, inventory, hotbar)


# create pygame sprite groups
item_group = pg.sprite.Group()
enemy_group = pg.sprite.Group()
player_group = pg.sprite.Group()
block_group = pg.sprite.Group()

# add sprites to groups
player_group.add(player)

# create map
gamemap = Map(r'map/Slime hunter graphics/map.tmx')
# create a game camera
camera = Camera(player, SCREEN.get_width(), SCREEN.get_height(),
                gamemap.width, gamemap.height)

# define a dict for all items
item_dict = {
    'apple': Apple,
    'sword': Sword,
    'leather_armor': LeatherArmor,
    'wooden_pickaxe': WoodenPickaxe,
    'coin': Coin
}

def fast_save():
    reset_file('save/player.pkl')
    for obj in player_group:
        save_object(obj, 'save/player.pkl')

    item_list = []
    for obj in item_group:
        saved_data = obj.get_save_data()
        item_list.append(saved_data)

    reset_file('save/item.pkl')
    save_to_file('save/item.pkl', item_list)

    enemy_list = []
    for obj in enemy_group:
        saved_data = obj.get_save_data()
        enemy_list.append(saved_data)

    reset_file('save/enemy.pkl')
    save_to_file('save/enemy.pkl', enemy_list)

    # save hotbar:
    reset_file('save/hotbar.pkl')
    save_to_file('save/hotbar.pkl', hotbar.get_save_data())

    # # save camera:
    # reset_file('save/camera.pkl')
    # save_to_file('save/camera.pkl', camera.get_save_data())
    
    # # save map"
    # reset_file('save/map.pkl')
    # save_to_file('save/map.pkl', gamemap.get_save_data())

    print('Saving')

# save every 20secs
def save_game(start_time=pg.time.get_ticks()):
    current = pg.time.get_ticks()
    if current - start_time > 20000:
        reset_file('save/player.pkl')
        for obj in player_group:
            save_object(obj, 'save/player.pkl')

        item_list = []
        for obj in item_group:
            saved_data = obj.get_save_data()
            item_list.append(saved_data)

        reset_file('save/item.pkl')
        save_to_file('save/item.pkl', item_list)

        enemy_list = []
        for obj in enemy_group:
            saved_data = obj.get_save_data()
            enemy_list.append(saved_data)

        reset_file('save/enemy.pkl')
        save_to_file('save/enemy.pkl', enemy_list)

        # save hotbar:
        reset_file('save/hotbar.pkl')
        save_to_file('save/hotbar.pkl', hotbar.get_save_data())

        # # save camera:
        # reset_file('save/camera.pkl')
        # save_to_file('save/camera.pkl', camera.get_save_data())
        
        # # save map"
        # reset_file('save/map.pkl')
        # save_to_file('save/map.pkl', gamemap.get_save_data())

        print('Saving')
        return current
    return start_time

def load_game():
    # empty each group first
    player_group.empty()
    load_object(player, 'save/player.pkl')
    player_group.add(player)

    # load hotbar
    hotbar.load_data(load_from_file('save/hotbar.pkl'), item_dict)

    # # load map
    # gamemap.load_data(load_from_file('save/map.pkl'))

    # # load camera
    # camera.load_data(load_from_file('save/camera.pkl'))

    item_group.empty()
    item_data_list = load_from_file('save/item.pkl')
    for data in item_data_list:
        item = item_dict[data['name']](
            0, 0, data['width'], data['height'], data['color'])
        item.load_data(data)
        item_group.add(item)

    enemy_group.empty()
    enemy_data_list = load_from_file('save/enemy.pkl')
    for data in enemy_data_list:
        enemy = Slime(0, 0, data['width'],
                      data['height'], data['color'], coin)
        enemy.load_data(data)
        enemy_group.add(enemy)

# show hp on top of the enemies
def show_hp(screen):
    status_bar.show_status(screen, player)
    for enemy in enemy_group:
        enemy.show_hp(screen)

gameplay = Gameplay(SCREEN)
gameplay.setup_map(gamemap)
gameplay.setup_entity_group(player_group, item_group, enemy_group, block_group)
gameplay.setup_inventory(inventory, hotbar)
gameplay.setup_utilities(camera, control, fast_save, fps_clock)
gameplay.setup_status(status_bar)
gameplay.create_enemy(Slime, COLOR['green'], coin)
gameplay.create_item(item_dict)
