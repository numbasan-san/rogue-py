
# from map_setings.game_map import Game_Map

import math
import tcod as libtcod

class Character:

    # general base to create any character I need
    def __init__(self, x, y, char, color, name, block = False, fighter = None, ai = None):
        self.x = x
        self.y = y
        self.char = char
        self.color = color
        self.name = name
        self.block = block
        self.fighter = fighter
        self.ai = ai

        if self.fighter:
            self.fighter.owner = self
        if self.ai:
            self.ai.owner = self
    
    def move(self, dx, dy): # character movement
        self.x += dx
        self.y += dy

    def move_towards(self, target_x, target_y, game_map, entities): # enemy automatic movement in x and y
        dx = target_x - self.x
        dy = target_y - self.y
        distance = math.sqrt((dx ** 2) + (dy ** 2))

        dx = int(round(dx / distance))
        dy = int(round(dy / distance))

        if not(game_map.is_blocked((self.x + dx), (self.y + dy)) or \
        self.collition_entity(entities, self.x + dx, self.y + dy)):
            self.move(dx, dy)

    def move_astar(self, target, entities, game_map): # enemy automatic movement in vertical, horizontal and diagonal
        fov = libtcod.map_new(game_map.w, game_map.h)

        for y1 in range(game_map.h):
            for x1 in range(game_map.w):
                fov.transparent[y1][x1] = not game_map.tiles[x1][y1].block_sight
                fov.walkable[y1][x1] = not game_map.tiles[x1][y1].blocked
        
        for entity in entities:
            if entity.block and entity != self and entity != target:
                fov.transparent[entity.y][entity.x] = True
                fov.walkable[entity.y][entity.x] = False
        
        my_path = libtcod.path_new_using_map(fov, 1.41)

        libtcod.path_compute(my_path, self.x, self.y, target.x, target.y)

        if not libtcod.path_is_empty(my_path) and libtcod.path_size(my_path) < 25:
            x, y = libtcod.path_walk(my_path, True)
            if x or y:
                self.x = x
                self.y = y
        else:
            self.move_towards(target.x, target.y, game_map, entities)
        
        libtcod.path_delete(my_path)
    
    def distance_to(self, other): # calculate distance between enemy and player
        dx = other.x - self.x
        dy = other.y - self.y
        return math.sqrt((dx ** 2) + (dy ** 2))

    @staticmethod
    def collition_entity(entities, coor_x, coor_y):  # name explain it self
        for entity in entities:
            if entity.block and entity.x == coor_x and entity.y == coor_y:
                return entity
        return None
