import pygame as pg
from pygame.locals import *
pg.init()


class Inventory:
    def __init__(self, capacity, hotbar):
        self.capacity = capacity
        self.stack_capacity = 16
        self.item_map = {}
        self.item_group = pg.sprite.Group()
        self.hotbar = hotbar
        self.open = False

    def add_item(self, item):
        # the format of 1 slot in the inventory is {item_name: number_of_item}
        '''
        There are 4 cases:
        1. The inventory is not full
        2. The inventory is full
        3. The item stack is full
        4. The hotbar is not full
        The item will fill up the hotbar first, then the inventory
        '''

        if self.hotbar.contain(item):
            self.hotbar.add_item(item)
            return

        if not self.hotbar.is_full():
            self.hotbar.add_item(item)
            return

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
        # print('Pick up', item.name.capitalize())
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
        print(f'Hotbar: {self.hotbar.hotbar_items}')
        print(f'Inventory: {self.item_map}')

    def toggle_inventory(self):
        if self.open:
            self.open = False
            print('Inventory closed')
        else:
            self.open = True
            print('Inventory opened')

    def draw(self, screen):
        self.hotbar.draw(screen)
        self.item_group.draw(screen)

    def get_save_data(self):
        data_dict = {'item_map': self.item_map, 'capacity': self.capacity,
                     'stack_capacity': self.stack_capacity}
        return data_dict

    def load_data(self, data_dict):
        self.item_map = data_dict['item_map']
        self.capacity = data_dict['capacity']
        self.stack_capacity = data_dict['stack_capacity']

    def empty(self):
        self.item_map = {}
        self.item_group.empty()

class HotBar(pg.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.width = width
        self.height = height
        self.color = color
        self.image = pg.Surface((self.width, self.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # set up font for the hotbar
        self.font = pg.font.SysFont('Arial', 14)
        self.font_color = self.color
        # transparent background
        self.font_bg = (255, 255, 255)

        # set up the hotbar algorithm
        self.current_slot = 0
        self.hotbar_length = 4

        # hotbar_slots link the keyboard's input with the item
        # self.hotbar_slots = {keyboard_input: item}
        self.hotbar_slots = {0: None, 1: None, 2: None, 3: None}

        # hotbar_items link the item with the quantity
        # self.hotbar_items = {item: quantity}
        self.hotbar_items = {}

    def current_item(self):
        return self.hotbar_slots[self.current_slot]

    # rewrite this function
    # it is taking the input from the keyboard
    # and check what is inside the current slot

    def select_slot(self, slot):
        self.current_slot = slot - 1
        # if self.current_item() != None:
        #     print(self.current_item().name)
        # else:
        #     print('Empty slot')

    def is_full(self):
        if None not in self.hotbar_slots.values():
            # print('Hotbar is full!')
            return True
        else:
            return False

    def add_item(self, item):
        # check if the item already exists in the hotbar
        # if it does, increase the quantity
        if item.name in self.hotbar_items:
            self.hotbar_items[item.name] += 1
            item.pickup()
            return

        # check if the hotbar is full
        if self.is_full():
            return

        # if the hotbar is not full, find an empty slot
        # and add the item to the hotbar

        for i in range(self.hotbar_length):
            if self.hotbar_slots[i] == None:
                self.hotbar_slots[i] = item
                self.hotbar_items[item.name] = 1
                item.pickup()
                break

    def contain(self, item):
        if item.name in self.hotbar_items:
            return True
        else:
            return False

    def draw(self, screen):
        box_x = self.rect.x
        box_y = self.rect.y
        box_width = self.width / self.hotbar_length
        box_height = self.height

        for i in range(self.hotbar_length):
            box = pg.Rect(box_x + box_width * i, box_y, box_width, box_height)
            pg.draw.rect(screen, self.color, box, 1)

            if self.hotbar_slots[i] != None:
                item_name = self.hotbar_slots[i].name
                item_quantity = self.hotbar_items[item_name]
                item_text = self.font.render(
                    item_name + ' ' + str(item_quantity), True, self.font_color, self.font_bg)
                item_text_rect = item_text.get_rect()
                item_text_rect.center = box.center
                screen.blit(item_text, item_text_rect)

        # highlight the current box in red
        current_box = pg.Rect(box_x + box_width *
                              self.current_slot, box_y, box_width, box_height)
        pg.draw.rect(screen, (255, 0, 0), current_box, 1)

    def get_save_data(self):
        save_data = []
        for item in self.hotbar_slots.values():
            if item != None:
                save_data.append(item.get_save_data())
            else:
                save_data.append(None)

        data_dict = {'hotbar_items': self.hotbar_items,
                     'hotbar_slots': save_data}
        return data_dict

    def load_data(self, data_dict, item_dict):

        self.hotbar_items = data_dict['hotbar_items']

        # This is a list of item
        # each element is a dictionary of item's data
        # we need to read the data and reconstruct with load_data method
        save_data = data_dict['hotbar_slots']
        for data in save_data:
            if data != None:
                item = item_dict[data['name']](0, 0, 0, 0, data['color'])
                item.load_data(data)
                self.hotbar_slots[save_data.index(data)] = item

    def empty(self):
        self.hotbar_items = {}
        self.hotbar_slots = {0: None, 1: None, 2: None, 3: None}

