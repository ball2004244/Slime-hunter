import pygame as pg
from pygame.locals import *

pg.init()


class Camera:
    def __init__(self, player, screen_width, screen_height, map_width, map_height):
        self.player = player
        self.x = 0
        self.y = 0
        self.width = screen_width
        self.height = screen_height
        self.map_width = map_width
        self.map_height = map_height

        # create a rect for the camera and center it in the screen
        self.rect = pg.Rect(0, 0, self.width, self.height)
        self.rect.center = (self.width / 2, self.height / 2)

        self.padding = 60
        self.padding_top = self.padding
        self.padding_left = self.padding
        self.padding_right = self.width - self.padding
        self.padding_bottom = self.height - self.padding

        self.speed = self.player.default_speed
        self.create_collision_points()
    '''
    CHECK COLLISION BETWEEN PLAYER AND PADDING
    '''
    def player_movement(self, _map):
        self.move_top(_map)
        self.move_bottom(_map)
        self.move_left(_map)
        self.move_right(_map)
        pass 

    def move_top(self, _map):
        if self.player.rect.y <= self.padding_top:
            self.player.top_transition = True
            
            self.collide_top(_map)
            return

        self.player.top_transition = False

    def move_bottom(self, _map):
        if self.player.rect.y + self.player.height >= self.padding_bottom:
            self.player.bottom_transition = True
            
            self.collide_bottom(_map)
            return

        self.player.bottom_transition = False

    def move_left(self, _map):
        if self.player.rect.x <= self.padding_left:
            self.player.left_transition = True
            
            self.collide_left(_map)
            return

        self.player.left_transition = False

    def move_right(self, _map):
        if self.player.rect.x + self.player.width >= self.padding_right:
            self.player.right_transition = True
        
            self.collide_right(_map)
            return

        self.player.right_transition = False

    '''
    CHECK THE COLLISION BETWEEN CAMERA AND MAP
    '''

    # create 4 points and place on 4 sides of the camera
    # check if the points are inside the map
    # if not, move the camera to the opposite direction
    # then use collidepoint() to check if the points are inside the map
    # if inside, then the camera can move
    # if not, then the camera can't move
    def create_collision_points(self):
        self.left_point = (self.x, self.y + self.height / 2)
        self.right_point = (self.x + self.width, self.y + self.height / 2)
        self.top_point = (self.x + self.width / 2, self.y)
        self.bottom_point = (self.x + self.width / 2, self.y + self.height)

    def collide_left(self, _map):
        if _map.rect.collidepoint(self.left_point):
            self.x -= self.speed
            _map.update(self.speed, 0)

    def collide_right(self, _map):
        if _map.rect.collidepoint(self.right_point):
            self.x += self.speed
            _map.update(-self.speed, 0)

    def collide_top(self, _map):
        if _map.rect.collidepoint(self.top_point):
            self.y -= self.speed
            _map.update(0, self.speed)

    def collide_bottom(self, _map):
        if _map.rect.collidepoint(self.bottom_point):
            self.y += self.speed       
            _map.update(0, -self.speed) 
    

    def update(self, _map):
        self.create_collision_points()
        self.player_movement(_map)

    def get_pos(self):
        return self.x, self.y


'''
DUMMY MAP for testing
'''


'''class Map:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        # import image
        self.image = pg.image.load('background.jpg')
        self.image = pg.transform.scale(self.image, (self.width, self.height))

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
'''