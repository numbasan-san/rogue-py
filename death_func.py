import tcod as libtcod

from game_state import Game_State


def kill_player(player):
    player.char = '%'
    player.color = libtcod.dark_red

    return 'You died!', Game_State.PLAYER_DEAD


def kill_monster(monster):
    death_message = '{0} is dead!'.format(monster.name.capitalize())
#  char, color, name, block=False, fighter=None, ai=None
    monster.char = '='
    monster.color = libtcod.dark_red
    monster.block = False
    monster.fighter = None
    monster.ai = None
    monster.name = 'remains of ' + monster.name

    return death_message