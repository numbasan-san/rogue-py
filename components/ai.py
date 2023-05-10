
class Monster:

    def take_turn(self, target, fov_map, game_map, entities): # name explain it self
        monster = self.owner
        result = []
        if fov_map.fov[monster.y][monster.x]:
            dist = monster.distance_to(target)
            if monster.distance_to(target) >= 2:
                monster.move_astar(target, entities, game_map)
            elif target.fighter.hp <= 0:
                print(f'{monster.name} said "damn camper".')
            elif target.fighter.hp > 0:
                pass
                '''
                attack_result = monster.fighter.attack(target)
                result.extend(attack_result)
                '''
        
        return result
