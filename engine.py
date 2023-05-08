
import sys, os, input_handler, render
from character import Character
import tcod as libtcod

DATA_FOLDER = 'data'
FONT_FILE = os.path.join(DATA_FOLDER, 'dejavu10x10_gs_tc.png')

def main():
    # screen size
    screen_w = 80
    screen_h = 50

    # entety declare
    player = Character(int(screen_w / 2), int(screen_h / 2), '@', libtcod.orange)
    npc = Character(int(screen_w / 2 - 5), int(screen_h / 2 - 5), '$', libtcod.purple)
    entities = [player, npc]

    #load screen
    libtcod.console_set_custom_font(FONT_FILE, libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
    libtcod.console_init_root(screen_w, screen_h, 'rogue-py', False)
    con = libtcod.console_new(screen_w, screen_h) # to update screen

    # keys variables declare
    key = libtcod.Key()
    mouse = libtcod.Mouse()

    while not libtcod.console_is_window_closed():
        # load screen elements
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)
        # libtcod.console_set_default_foreground(con, libtcod.white)
        # libtcod.console_put_char(con, player.x, player.y, player.char, libtcod.BKGND_NONE)
            # "refresh" the screen
        # libtcod.console_blit(con, 0, 0, screen_w, screen_h, 0, 0, 0)
        render.render_all(con, entities, screen_w, screen_h)
        libtcod.console_flush()
        # libtcod.console_put_char(con, player.x, player.y, ' ', libtcod.BKGND_NONE)
        render.clear_all(con, entities)

        # key effects/actions
        action = input_handler.keys_comands(key)

        move = action.get('move')
        exit = action.get('exit')
        fullscreen = action.get('fullscreen')

        if move:
            dx, dy = move
            player.move(dx, dy)
        if exit:
            return True
        
        if fullscreen:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen)



if __name__ == "__main__":
    main()
