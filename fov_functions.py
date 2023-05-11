
import tcod as libtcod

def init_fov(game_map):
    fov_map = libtcod.map_new(game_map.w, game_map.h)
    for y in range(game_map.h):
        for x in range(game_map.w):
            fov_map.transparent[y][x] = not game_map.tiles[x][y].block_sight
            fov_map.walkable[y][x] = not game_map.tiles[x][y].blocked
    return fov_map

def recompute_fov(fov_map, x, y, radius, light_walls, algorithm = 0):
    fov_map.compute_fov(x, y, radius, light_walls, algorithm)
