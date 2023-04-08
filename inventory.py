import pygame as pg
from pygame.locals import *

pg.init()

class Inventory:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack_capacity = 16
        self.item_map = {}
        self.item_group = pg.sprite.Group()

    def add_item(self, item, hotbar): 
        # the format of 1 slot in the inventory is {item_name: number_of_item}
        '''
        There are 4 cases:
        1. The inventory is not full
        2. The inventory is full
        3. The item stack is full
        4. The hotbar is not full
        '''

        # case 4
        hotbar.add_item(item)


        if not item.name in self.item_map:
            if len(self.item_map) >= self.capacity:
                print('Inventory is full!')
                return 
            
            self.item_map[item.name] = 1
            self.item_group.add(item)

        else:
            if self.item_map[item.name] >= self.stack_capacity:
                print('Item stack is full!')
                return 
            
            self.item_map[item.name] += 1

        item.pickup()
        print('Pick up', item.name.capitalize())
        return 

    def remove_item(self, item):
        if item.name in self.item_map:
            self.item_map[item.name] -= 1
            if self.item_map[item.name] <= 0:
                del self.item_map[item.name]
                self.item_group.remove(item)
    
    # get a number of a specific item
    def get_item(self, item_name):
        if item_name in self.item_map:
            return self.item_map[item_name]
        
    def open_inventory(self):
        print(self.item_map)


# create a UI for the inventory
class InventoryUI:
    def __init__(self, inventory):
        self.inventory = inventory
        self.item_group = inventory.item_group
        self.item_map = inventory.item_map
        self.item_list = []

        self.item_font = pg.font.SysFont('Arial', 20)
        self.item_font_color = (0, 0, 0)
        self.item_font_bg = (255, 255, 255)

    def draw(self, screen):
        self.item_list = []
        for item in self.item_group:
            self.item_list.append(item)
        
        for i in range(len(self.item_list)):
            item = self.item_list[i]
            item_text = self.item_font.render(item.name, True, self.item_font_color, self.item_font_bg)
            item_text_rect = item_text.get_rect()
            item_text_rect.x = 10
            item_text_rect.y = 10 + i * 30
            screen.blit(item_text, item_text_rect)


class HotBar(pg.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.image = pg.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.current_slot = 0
        self.empty_slot = None
        self.hotbar_length = 4

        # hotbar_slots link the keyboard's input with the item
        self.hotbar_slots = {0: None, 1: None, 2: None, 3: None}

        # hotbar_items link the item with the quantity
        self.hotbar_items = {None: 0, None: 0, None: 0, None: 0}

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def current_item(self):
        return self.hotbar_slots[self.current_slot]

    def select_slot(self, slot):
        self.current_slot = slot - 1
        if self.current_item() != None:
            print(self.current_item().name)
        else:
            print('Empty slot')

    def add_item(self, item):
        # check if the item already exists in the hotbar
        # if it does, increase the quantity
        if item.name in self.hotbar_items:
            self.hotbar_items[item.name] += 1
            return

        # check if the hotbar is full
        if None not in self.hotbar_slots.values():
            print('Hotbar is full!')
            return
        
        # if the hotbar is not full, find an empty slot
        # and add the item to the hotbar
        self.empty_slot = None
        for i in range(self.hotbar_length):
            if self.hotbar_slots[i] == None:
                self.empty_slot = i
                break
        
        self.hotbar_slots[self.empty_slot] = item
        self.hotbar_items[item.name] = 1



        
