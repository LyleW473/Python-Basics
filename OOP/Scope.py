class Hero:
    def __init__(self, damage, monster):
        self.damage = damage
        self.monster = monster  

    def attack(self):
        self.monster.get_damage(self.damage)


class Monster:
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy
        print(f"The monster was created with {self.health} HP and {self.energy} energy!")

    # Methods
    def get_damage(self, amount):
        self.health -= amount



monster1 = Monster(1000, 50)

hero = Hero(damage = 100, monster = monster1)

hero.attack()

print(monster1.health)