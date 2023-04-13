'''import pygame
import pytmx
import os

class TileMap:
    def __init__(self, filename):
        self.tmx_data = pytmx.load_pygame(filename)

        self.width = self.tmx_data.width * self.tmx_data.tilewidth
        self.height = self.tmx_data.height * self.tmx_data.tileheight

    def render(self, surface):
        ti = self.tmx_data.get_tile_image_by_gid
        for layer in self.tmx_data.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile = ti(gid)
                    if tile:
                        surface.blit(tile, (x * self.tmx_data.tilewidth, y * self.tmx_data.tileheight))

    def get_tile_properties(self, x, y, layer):
        tile_gid = self.tmx_data.layers[layer].data[y][x]
        tile_properties = self.tmxx_data.get_tile_properties_by_gid(tile_gid)
        return tile_properties

    def get_tile_rect(self, x, y):
        return pygame.Rect(x * self.tmx_data.tilewidth, y * self.tmx_data.tileheight, self.tmx_data.tilewidth, self.tmx_data.tileheight)


class Camera:
    def __init__(self, width, height, tile_map):
        self.width = width
        self.height = height
        self.tile_map = tile_map
        self.state = pygame.Rect(0, 0, self.width, self.height)

    def apply(self, rect):
        return rect.move(self.state.topleft)

    def update(self, player_rect):
        x = -player_rect.x + int(self.width / 2)
        y = -player_rect.y + int(self.height / 2)
        x = min(0, x)  # left
        y = min(0, y)  # top
        x = max(-(self.tile_map.width - self.width), x)  # right
        y = max(-(self.tile_map.height - self.height), y)  # bottom
        self.state = pygame.Rect(x, y, self.tile_map.width, self.tile_map.height)

    def draw(self, screen, background):
        screen.blit(background, self.apply(background.get_rect()))


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((32, 32))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, x, y):
        self.rect.x += x
        self.rect.y += y


def main():
    # Initialize pygame
    pygame.init()

    # Set up the screen
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Tilemap")

    # Load the tile map
    tile_map = TileMap(os.path.join("map", "Slime hunter graphics", "map.tmx"))

    # Create the camera
    camera = Camera(screen_width, screen_height, tile_map)

    # Create the player
    player = Player(0, 0)
    player_group = pygame.sprite.Group(player)

    # Create the background
    # this create a surface the size of the map
    # which means that the map will be drawn on this surface
    # then what we do is to move this surface around
    background = pygame.Surface((tile_map.width, tile_map.height))
    tile_map.render(background)

    # Set up the game loop
    clock = pygame.time.Clock()
    running = True

    # Main game loop
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update the player position
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.update(-5, 0)
        if keys[pygame.K_RIGHT]:
            player.update(5, 0)
        if keys[pygame.K_UP]:
            player.update(0, -5)
        if keys[pygame.K_DOWN]:
            player.update(0, 5)

        # Update the camera position
        camera.update(player.rect)

        # Draw the background and sprites
        camera.draw(screen, background)
        player_group.draw(screen)

        # Update the display
        pygame.display.update()

        # Cap the frame rate
        clock.tick(60)

    # Quit pygame
    pygame.quit()


if __name__ == '__main__':
    main()

'''

import pygame as pg
from pygame.locals import *
import pytmx
from setup import SCREEN, COLOR, window_setup, FPS_clock
from __init__ import *


pg.init()

class Tile(pg.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)

class Map:
    def __init__(self, filename):
        self.tmx_data = pytmx.util_pygame.load_pygame(filename)

        self.image_dict = {}
        self.tile_sprites = pg.sprite.Group()
        self.x = 0
        self.y = 0
        self.load_game()

    def load_map(self):
        for layer in self.tmx_data.visible_layers:
            if hasattr(layer, 'data'):
                for x, y, surf in layer.tiles():
                    pos = (x * self.tmx_data.tilewidth, y * self.tmx_data.tileheight)
                    Tile(pos=pos, surf=surf, groups=self.tile_sprites)

    def load_objects(self):
        for obj in self.tmx_data.objects:
            pos = obj.x, obj.y
            if obj.image:
                Tile(pos=pos, surf=obj.image, groups=self.tile_sprites)

    def load_game(self):
        self.load_map()
        self.load_objects()

    def render(self, screen):
        self.tile_sprites.draw(screen)

    def update_position(self, dx, dy):
        self.x += dx
        self.y += dy
        for sprite in self.tile_sprites:
            sprite.rect.move_ip(dx, dy)

if __name__ == '__main__':
    screen = pg.display.set_mode((800, 600))
    _map = Map(r'map/Slime hunter graphics/map.tmx')

    background = pg.Surface(screen.get_size())
    background.fill((255, 255, 255))
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

            keys = pg.key.get_pressed()   
            if keys[K_LEFT] or keys[K_a]:
                _map.update_position(10, 0)
            if keys[K_RIGHT] or keys[K_d]:
                _map.update_position(-10, 0)
            if keys[K_UP] or keys[K_w]:
                _map.update_position(0, 10)
            if keys[K_DOWN] or keys[K_s]:
                _map.update_position(0, -10)

        screen.blit(background, (0, 0))
        _map.render(screen)
        SCREEN.fill(COLOR['white'])

    
        player_group.draw(SCREEN)
        enemy_group.draw(SCREEN)
        item_group.draw(SCREEN)
        """ block_group.draw(SCREEN) """

        # show status
        hotbar.draw(SCREEN)
        show_hp(SCREEN)

        # slime1.random_movement(movement, camera)

        # process the user keyboard + mouse input
        control.event_loop(player_group, item_group, enemy_group, block_group)            

        camera.update(gamemap)
        pg.display.update()

    pg.quit()