'''
* = Wall
Space = Route
O = Obstacle
E = Enemy
N = NPC
P = Player

default size: 1920 x 1080
'''
'''

import os
import pygame
import pytmx

pygame.init()

# This is the class for the tiles
# 1 tile = 16 pixels
class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft = pos)

screen = pygame.display.set_mode((1920, 1080))

# Load the map
tmx_data = pytmx.util_pygame.load_pygame(r'Slime hunter graphics/map.tmx')

""" tileset_image = pygame.image.load(r'Slime hunter graphics/assets/terrain_with_shadows.png') """

# Load the tileset images
path = r'Slime hunter graphics/assets'
image_dict = {}

# the tileset is a collection of images
# the image_dict is a dictionary of the images in the tileset
for filename in os.listdir(path):
    if filename.endswith('.png'):
        image_path = os.path.join(path, filename)
        image_name = os.path.splitext(filename)[0]
        image_dict[image_name] = pygame.image.load(image_path)

tile_sprites = pygame.sprite.Group()

# load map
for layer in tmx_data.visible_layers:
    if hasattr(layer, 'data'):
        for x, y, surf in layer.tiles():
            pos = (x * tmx_data.tilewidth, y * tmx_data.tileheight)
            Tile(pos = pos, surf = surf, groups = tile_sprites)

# load objects on map
for obj in tmx_data.objects:
    pos = obj.x, obj.y
    if obj.image:
        Tile(pos = pos, surf = obj.image, groups = tile_sprites)

def main():
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Clear the screen
        screen.fill((0, 0, 0))
        
        # Draw the tile sprites
        tile_sprites.draw(screen)

        # Draw the shapes obj (currently not have in map)
        """ for obj in tmx_data.objects:
            pos = obj.x, obj.y
            if obj.type == 'Shapes':
                if obj.name == 'name':
                    print(obj.x)
                    print(obj.y) """
        
        # Update the display
        pygame.display.update()

    # Quit Pygame when the game loop ends
    pygame.quit()

if __name__ == '__main__':
    main()'''

import pygame as pg
from pygame.locals import *
import pytmx

pg.init()

class Tile(pg.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft = pos)

class Map:
    def __init__(self, filename):
        self.tmx_data = pytmx.util_pygame.load_pygame(filename)

        self.image_dict = {}
        self.tile_sprites = pg.sprite.Group()
        self.x = 0
        self.y = 0
        self.width = self.tmx_data.width * self.tmx_data.tilewidth
        self.height = self.tmx_data.height * self.tmx_data.tileheight

        # create a rect for the map and center it
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)
        self.rect.center = (self.width / 2, self.height / 2)
        
        self.load_game()

    def load_map(self):
        for layer in self.tmx_data.visible_layers:
            if hasattr(layer, 'data'):
                for x, y, surf in layer.tiles():
                    pos = (x * self.tmx_data.tilewidth, y * self.tmx_data.tileheight)
                    Tile(pos = pos, surf = surf, groups = self.tile_sprites)

    def load_objects(self):
        for obj in self.tmx_data.objects:
            pos = obj.x, obj.y
            if obj.image:
                Tile(pos = pos, surf = obj.image, groups = self.tile_sprites)
            
    def load_game(self):
        self.load_map()
        self.load_objects()

    def render(self, screen):
        self.tile_sprites.draw(screen)

    def update(self, x, y):
        # validate if the map is going to be out of the screen
        move_x = x
        move_y = y
        # if self.x + x < 0 or self.x + x > self.width:
        #     move_x = 0

        # if self.y + y < 0 or self.y + y > self.height:
        #     move_y = 0

        self.x += move_x
        self.y += move_y
        for sprite in self.tile_sprites:
            sprite.rect.move_ip(move_x, move_y)
if __name__ == '__main__':
    screen = pg.display.set_mode((1920, 1080))
    _map = Map(r'Slime hunter graphics/map.tmx')
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        screen.fill((0, 0, 0))
        _map.draw(screen)
        pg.display.update()

    pg.quit()