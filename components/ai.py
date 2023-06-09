
import tcod as libtcod


class Monster:
    def take_turn(self, target, fov_map, game_map, entities):
        result = []
        monster = self.owner
        if libtcod.map_is_in_fov(fov_map, monster.x, monster.y):

            if monster.distance_to(target) >= 2:
                # monster.move_towards(target.x, target.y, game_map, entities)
                monster.move_astar(target, entities, game_map)

            elif target.fighter.hp > 0:
                attack_results = monster.fighter.attack(target)
                result.extend(attack_results)
                # print(f'The {monster.name} insults you! Your ego is damaged!')

        return result
