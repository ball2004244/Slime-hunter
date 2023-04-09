# create a camera class to follow the player
# the camera will move if the user touch the padding
# character/player.py
# setup.py <-> config.cfg
# main.py
# __init__.py
# map/map.py

class Camera:
    def __init__(self, player, screen_width, screen_height, map_width, map_height):
        self.player = player
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.map_width = map_width
        self.map_height = map_height
        self.padding = 100
        self.padding_top = self.padding
        self.padding_left = self.padding
        self.padding_right = self.screen_width - self.padding
        self.padding_bottom = self.screen_height - self.padding

    def update(self):
        # Move the camera if the player is close to the edge of the screen
        print(self.player.rect.x, self.player.rect.y)
        touching_padding = False
        if self.player.rect.x <= self.padding_left:
            self.speed = self.player.speed
            self.player.speed = 0
            touching_padding = True
        elif self.player.rect.x >= self.padding_right:
            self.speed = self.player.speed
            self.player.speed = 0
            touching_padding = True
       
        if self.player.rect.y <= self.padding_top:
            self.speed = self.player.speed
            self.player.speed = 0
            touching_padding = True
        elif self.player.rect.y >= self.padding_bottom:
            self.speed = self.player.speed
            self.player.speed = 0
            touching_padding = True
        
        if not touching_padding:
            self.player.speed = 3
            

    def apply(self, rect):
        # Shift the rectangle by the camera position
        return rect.move(-self.x, -self.y)

