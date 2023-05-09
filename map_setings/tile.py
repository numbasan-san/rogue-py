
class Tile:

    # general base to create any room I need
    def __init__(self, blocked, block_sight = None, explored = False):
        self.blocked = blocked

        if block_sight is None:
           block_sight = blocked
           
        self.block_sight = block_sight
        self.explored = explored
