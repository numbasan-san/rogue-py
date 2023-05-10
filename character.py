
# from map_setings.game_map import Game_Map

class Character:

    # general base to create any character I need
    def __init__(self, x, y, char, color, name, block = False):
        self.x = x
        self.y = y
        self.char = char
        self.color = color
        self.name = name
        self.block = block
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    @staticmethod
    def collition_entity(entities, coor_x, coor_y):
        for entity in entities:
            if entity.block and entity.x == coor_x and entity.y == coor_y:
                return entity
        return None
