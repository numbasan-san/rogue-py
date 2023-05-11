
class Monster:
    def take_turn(self, target, fov_map, game_map, entities):
        monster = self.owner
        result = []
        if fov_map.fov[monster.y][monster.x]:
            dist = monster.distance_to(target)
            if monster.distance_to(target) >= 2:
                # monster.move_towards(target.x, target.y, game_map, entities)
                monster.move_astar(target, entities, game_map)
            elif target.fighter.hp <= 0:
                print(f'{monster.name} said "damn camper".')
        # print(f'{self.owner.name} wonders when it will get to move.')
