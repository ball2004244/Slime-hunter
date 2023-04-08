'''
* = Wall
Space = Route
O = Obstacle
E = Enemy
N = NPC
P = Player

default size: 40x40
'''
import pygame
import pytmx

pygame.init()

screen = pygame.display.set_mode((1920, 1080))

tmx_data = pytmx.util_pygame.load_pygame(r'Slime hunter graphics/map.tmx')

tileset_image = pygame.image.load(r'Slime hunter graphics/assets/terrain_with_shadows.png')

# screen_width, screen_height = tmx_data.width * tmx_data.tilewidth, tmx_data.height * tmx_data.tileheight
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption("Slime Hunter")

tile_sprites = pygame.sprite.Group()

for layer in tmx_data.visible_layers:
    for x, y, gid in layer:
        tile = tmx_data.get_tile_image_by_gid(gid)
        if tile:
            tile_sprite = pygame.sprite.Sprite()
            tile_sprite.image = tile
            tile_sprite.rect = tile.get_rect()
            tile_sprite.rect.x = x * tmx_data.tilewidth
            tile_sprite.rect.y = y * tmx_data.tileheight
            tile_sprites.add(tile_sprite)

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
        
        # Update the display
        pygame.display.flip()

    # Quit Pygame when the game loop ends
    pygame.quit()

if __name__ == '__main__':
    main()