'''
* = Wall
Space = Route
O = Obstacle
E = Enemy
N = NPC
P = Player

default size: 40x40
'''

import os
import pygame
import pytmx

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft = pos)

pygame.init()

screen = pygame.display.set_mode((1920, 1080))

tmx_data = pytmx.util_pygame.load_pygame(r'Slime hunter graphics/map.tmx')

""" tileset_image = pygame.image.load(r'Slime hunter graphics/assets/terrain_with_shadows.png') """

path = r'Slime hunter graphics/assets'
image_dict = {}

for filename in os.listdir(path):
    if filename.endswith('.png'):
        image_path = os.path.join(path, filename)
        image_name = os.path.splitext(filename)[0]
        image_dict[image_name] = pygame.image.load(image_path)

tile_sprites = pygame.sprite.Group()

for layer in tmx_data.visible_layers:
    if hasattr(layer, 'data'):
        for x, y, surf in layer.tiles():
            pos = (x * tmx_data.tilewidth, y * tmx_data.tileheight)
            Tile(pos = pos, surf = surf, groups = tile_sprites)

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
    main()