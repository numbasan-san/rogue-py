
import tcod as libtcod
from game_state import Game_State

def kill_player(player):
    player.char = '/'
    player.color = libtcod.dark_red
    return 'YOU DIED!', Game_State.PLAYER_DEAD

def kill_monster(monster):
    death_message = f'{monster.name.capitalize()} is dead!'

    monster.char = '%'
    monster.color = libtcod.dark_red
    monster.block = False
    monster.fighter = None
    monster.ai = None
    monster.name = f'remains of {monster.name}'

    return death_message
