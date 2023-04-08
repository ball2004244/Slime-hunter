import pygame as pg
from pygame.locals import *

pg.init()

class Inventory:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack_capacity = 16
        self.item_map = {}
        self.item_group = pg.sprite.Group()
        
    def add_item(self, item): 

        '''
        There are 3 cases:
        1. The inventory is not full
        2. The inventory is full
        3. The item stack is full
        '''
        
        if not item.name in self.item_map:
            if len(self.item_map) >= self.capacity:
                print('Inventory is full!')
                return False
            
            self.item_map[item.name] = 1
            self.item_group.add(item)

        else:
            if self.item_map[item.name] >= self.stack_capacity:
                print('Item stack is full!')
                return False
            
            self.item_map[item.name] += 1

        item.pickup()
        print('Pick up', item.name.capitalize())
        return True

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