
class Fighter:
    def __init__(self, hp, defense, power):
        self.max_hp = hp
        self.hp = hp
        self.defense = defense
        self.power = power

    def take_damage(self, amount):
        result = []
        self.hp -= amount
        '''
        if self.hp <= 0:
            result.append({'dead': self.owner})
         
        return result
        '''

    def attack(self, target):
        result = []
        damage = self.power - target.fighter.defense

        if damage > 0:
            # result.append({'message': f'{self.owner.name.capitalize()} attacks {target.name} for {damage} DP.'})
            # result.extend(target.fighter.take_damage(damage))
            print(f'{self.owner.name.capitalize()} attacks {target.name} for {damage} DP.')
        else:
            '''result.append({
                'message': f'{self.owner.name.capitalize()} attacks {target.name} but does no damage.'
            })'''
            print(f'{self.owner.name.capitalize()} attacks {target.name} but does no damage.')
        
        # return result
