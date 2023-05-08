
import tcod as libtcod

def render_all(con, entites, screen_w, screen_h):
    for entity in entites:
        draw_entity(con, entity)

        libtcod.console_blit(con, 0, 0, screen_w, screen_h, 0, 0, 0)

def clear_all(con, entities):
    for entity in entities:
        clear_entity(con, entity)

def draw_entity(con, entity):
    libtcod.console_set_default_foreground(con, entity.color)
    libtcod.console_put_char(con, entity.x, entity.y, entity.char, libtcod.BKGND_NONE)

def clear_entity(con, entity):
    libtcod.console_put_char(con, entity.x, entity.y, ' ', libtcod.BKGND_NONE)
