
class Fighter:
    def __init__(self, hp, defense, power):
        self.max_hp = hp
        self.hp = hp
        self.defense = defense
        self.power = power

    def take_damage(self, amount):
        results = []

        self.hp -= amount

        if self.hp <= 0:
            results.append({'dead': self.owner})

        return results

    def attack(self, target):
        result = []
        damage = self.power - target.fighter.defense

        if damage > 0:
            result.append(
                {'message': f'{self.owner.name.capitalize()} attacks {target.name} for {str(damage)} hit points.'}
            )
            result.extend(target.fighter.take_damage(damage))
        else:
            result.append(
                {'message': f'{self.owner.name.capitalize()} attacks {target.name} but does no damage.'}
            )

        return result
