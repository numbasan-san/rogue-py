
import tcod as libtcod

def keys_comands(key):
    # Movement
    if key.vk == libtcod.KEY_UP:
        return {'move': (0, -1)}
    elif key.vk == libtcod.KEY_RIGHT:
        return {'move': (1, 0)}
    elif key.vk == libtcod.KEY_DOWN:
        return {'move': (0, 1)}
    elif key.vk == libtcod.KEY_LEFT:
        return {'move': (-1, 0)}
    '''
    elif key.vk == (libtcod.KEY_RIGHT and libtcod.KEY_DOWN):
        return {'move': (1, 1)}
    '''

    # keyboard attachment
    if key.vk == (libtcod.KEY_ENTER and key.lalt): # Fullscreen
        return {'fullscreen': True}
    elif key.vk == libtcod.KEY_ESCAPE: # Exit
         return {'exit': True}

    return {}
