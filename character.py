
from map_setings.game_map import Game_Map

class Character:

    # general base to create any character I need
    def __init__(self, x, y, char, color):
        self.x = x
        self.y = y
        self.char = char
        self.color = color
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
