
import sys, os, input_handler, render, fov_functions
from death_func import *
from game_state import Game_State
from components.fighter import Fighter
from map_setings.game_map import Game_Map
from character import Character
import tcod as libtcod

DATA_FOLDER = 'data'
FONT_FILE = os.path.join(DATA_FOLDER, 'dejavu10x10_gs_tc.png')

def main():

    # screen size
    screen_w = 80
    screen_h = 50

    # map size
    map_w = 80
    map_h = 45

    # romms size and number
    room_max_size = 16
    room_min_size = 6
    max_rooms = 30

    # fov
    fov_algorithm = 0
    fov_light_walls = True
    fov_radius = 30

    # max monster per room
    max_monsters_room = 5

    colors = {
        'dark_wall': libtcod.Color(0, 50, 100),
        'dark_ground': libtcod.Color(75, 75, 100),
        'light_wall': libtcod.Color(130, 110, 50),
        'light_ground': libtcod.Color(200, 180, 50)
    }

    fov_recompute = True

    # map declare
    game_map = Game_Map(map_w, map_h)

    # enteties declare
    fighter_component = Fighter(hp=30, defense=3, power=5)
    player = Character(int(screen_w / 2), int(screen_h / 2), '@', libtcod.orange, 'player', block = True, fighter=fighter_component)
    # npc = Character(int(screen_w / 2 - 5), int(screen_h / 2 - 5), '$', libtcod.purple)
    entities = [player]
    game_map.make_map(max_rooms, room_min_size, room_max_size, map_w, map_h, player, entities, max_monsters_room) # create map

    #load screen
    libtcod.console_set_custom_font(FONT_FILE, libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
    libtcod.console_init_root(screen_w, screen_h, 'rogue-py', False)
    con = libtcod.console_new(screen_w, screen_h) # to update screen

    # keys variables declare
    key = libtcod.Key()
    mouse = libtcod.Mouse()
    fov_map = fov_functions.init_fov(game_map)

    while not libtcod.console_is_window_closed():
        if fov_recompute:
            fov_functions.recompute_fov(fov_map, player.x, player.y, fov_radius, fov_light_walls, fov_algorithm)

        # load screen elements
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)
        render.render_all(con, entities, game_map, fov_map, fov_recompute, screen_w, screen_h, colors) # render all elements
        libtcod.console_flush()
        render.clear_all(con, entities)

        # key effects/actions
        action = input_handler.keys_comands(key)
        gs = Game_State.PLAYERS_TURN

        move = action.get('move')
        exit = action.get('exit')
        fullscreen = action.get('fullscreen')
        player_turn_results = []        

        if move and gs == Game_State.PLAYERS_TURN:
            dx, dy = move
            if not game_map.is_blocked(player.x + dx, player.y + dy): # wall collision
                coor_x = player.x + dx
                coor_y = player.y + dy
                target = player.collition_entity(entities, coor_x, coor_y)
                if target:
                    # print(f'{target.name} in the way.')
                    attack_results = player.fighter.attack(target)
                    player_turn_results.extend(attack_results)
                else:
                    fov_recompute = True
                    player.move(dx, dy)

                gs = Game_State.ENEMY_TURN
        if exit:
            return True
        
        if fullscreen:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen)
        
        for result in player_turn_results:
            message = result.get('message')
            dead_entity = result.get('dead')
            if message:
                print(message)
            if dead_entity:
                if dead_entity == player:
                    message, game_state = kill_player(dead_entity)
                else:
                    message = kill_monster(dead_entity)
                print(message)

        if gs == Game_State.ENEMY_TURN:
            for entity in entities:
                if entity.ai and fov_map.fov[entity.y][entity.x]:
                    enemy_turn_results = entity.ai.take_turn(player, fov_map, game_map, entities)
                    for result in enemy_turn_results:
                        message = result.get('message')
                        dead_entity = result.get('dead')
                        if message:
                            print(message)
                        if dead_entity:
                            if dead_entity == player:
                                message, gs = kill_player(dead_entity)
                            else:
                                message = kill_monster(dead_entity)
                            print(message)
                            if gs == Game_State.PLAYERS_TURN:
                                break
                    if gs == Game_State.PLAYERS_TURN:
                        break

            else:
                gs = Game_State.PLAYERS_TURN



if __name__ == "__main__":
    main()
