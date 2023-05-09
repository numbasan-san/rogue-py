
import random
import tcod as libtcod
from character import Character
from map_setings.rectangle import Rect
from map_setings.tile import Tile

class Game_Map:

    # map generation asets
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.tiles = self.init_tiles()

    def init_tiles(self): # init rooms basic elements
        tiles = [[Tile(True) for y in range(self.h)] for x in range(self.w)]
        
        return tiles
    
    def make_map(self, max_rooms, room_min_size, room_max_size, map_w, map_h, player, entities, max_monsters_room): # map creation
        
        rooms = []
        num_rooms = 0

        for r in range(max_rooms):
            # set coors and dimentions of any room
            w = random.randint(room_min_size, room_max_size)
            h = random.randint(room_min_size, room_max_size)
            x = random.randint(0, map_w - w - 1)
            y = random.randint(0, map_h - h - 1)

            new_room = Rect(x, y, w, h) # set a new room
            for other_room in rooms:
                if new_room.intersect(other_room): # prevente cross rooms
                    break
            else: # create new room if there isn't problems
                self.create_room(new_room)
                (new_x, new_y) = new_room.center()

                if num_rooms == 0:
                    player.x = new_x
                    player.y = new_y
                else: # create connection between rooms
                    (prev_x, prev_y) = rooms[num_rooms - 1].center()
                    if random.randint(0, 1) == 1:
                        self.create_h_tunnel(prev_x, new_x, prev_y)
                        self.create_v_tunnel(prev_y, new_y, new_x)
                    else:
                        self.create_v_tunnel(prev_y, new_y, prev_x)
                        self.create_h_tunnel(prev_x, new_x, new_y)
            self.place_entities(new_room, entities, max_monsters_room)
            rooms.append(new_room)
            num_rooms += 1

    def create_room(self, room): # create the room
        for x in range(room.x1 + 1, room.x2): # starts at "x1 + 1" to build the walls
            for y in range(room.y1 + 1, room.y2):
                self.tiles[x][y].blocked = False
                self.tiles[x][y].block_sight = False

    def create_h_tunnel(self, x1, x2, y): # horizontal tunnels
        for x in range(min(x1, x2), max(x1, x2) + 1):
            self.tiles[x][y].blocked = False
            self.tiles[x][y].block_sight = False

    def create_v_tunnel(self, y1, y2, x):# vertical tunnels
        for y in range(min(y1, y2), max(y1, y2) + 1):
            self.tiles[x][y].blocked = False
            self.tiles[x][y].block_sight = False

    def is_blocked(self, x, y): # set tiles collision
        if self.tiles[x][y].blocked:
            return True
        return False

    def place_entities(self, room, entities, max_monsters_room): # load enemies
        
        num_monsters = random.randint(0, max_monsters_room)

        for i in range(num_monsters):
            x = random.randint(room.x1 + 1, room.y2 - 1)
            y = random.randint(room.y1 + 1, room.y2 - 1)
            if not any([entity for entity in entities if entity.x == x and entity.y == y]):
                if random.randint(0, 100) < 80: 
                    monster = Character(x, y, 'o', libtcod.desaturated_green)
                else:
                    monster = Character(x, y, 'o', libtcod.darker_green)
                entities.append(monster)