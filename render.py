
import tcod as libtcod

def render_all(con, entites, game_map, fov_map, fov_recompute, screen_w, screen_h, colors):
    if fov_recompute:
        for y in range(game_map.h): # all estructures are rendered
            for x in range(game_map.w):
                visible = fov_map.fov[y][x]
                wall = game_map.tiles[x][y].block_sight
                if visible: # light all what is inside player's fov                    
                    if wall:
                        libtcod.console_set_char_background(con, x, y, colors.get('light_wall'), libtcod.BKGND_SET)
                    else:
                        libtcod.console_set_char_background(con, x, y, colors.get('light_ground'), libtcod.BKGND_SET)
                    game_map.tiles[x][y].explored = True
                elif game_map.tiles[x][y].explored:
                    if wall:
                        libtcod.console_set_char_background(con, x, y, colors.get('dark_wall'), libtcod.BKGND_SET)
                    else:
                        libtcod.console_set_char_background(con, x, y, colors.get('dark_ground'), libtcod.BKGND_SET)

    for entity in entites: # all entities are rendered
        if fov_map.fov[entity.y][entity.x]:
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
