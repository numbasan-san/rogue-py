
import tcod as libtcod

def render_all(con, entites, game_map, screen_w, screen_h, colors):

    for y in range(game_map.h): # all estructures are rendered
        for x in range(game_map.w):
            wall = game_map.tiles[x][y].block_sight

            if wall:
                libtcod.console_set_char_background(con, x, y, colors.get('dark_wall'), libtcod.BKGND_SET)
            else:
                libtcod.console_set_char_background(con, x, y, colors.get('dark_ground'), libtcod.BKGND_SET)

    for entity in entites: # all entities are rendered
        draw_entity(con, entity)

        libtcod.console_blit(con, 0, 0, screen_w, screen_h, 0, 0, 0)

def clear_all(con, entities): # clear all elements
    for entity in entities:
        clear_entity(con, entity)

def draw_entity(con, entity): # name explain it self
    libtcod.console_set_default_foreground(con, entity.color)
    libtcod.console_put_char(con, entity.x, entity.y, entity.char, libtcod.BKGND_NONE)

def clear_entity(con, entity): # name explain it self
    libtcod.console_put_char(con, entity.x, entity.y, ' ', libtcod.BKGND_NONE)
