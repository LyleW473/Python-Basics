""" Simple inheritance, for example could be one Parent class and one Child class """

class Monster:
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy

    def attack(self, amount):
        print("The monster has attacked!")
        print(f'{amount} damage was dealt')
        self.energy -= 20

    def move(self, speed):
        print(f'The monster now moves at a speed of {speed}.')


class Shark(Monster):
    def __init__(self, speed, health, energy):
        #Monster.__init__(self, health, energy) This is the old method of doing it
        super().__init__(health, energy) # This is the new method, this inherits Monster as well and does the same thing as the one above
        super().move(10) # Can call the move method of the superclass
        self.speed = speed

    def bite(self):
        print("The shark has bitten")

    def move(self):
        print(f"The speed of the shark is {self.speed}")


shark = Shark(speed = 120, health = 100, energy = 80)
print(shark.health)
shark.bite()
shark.attack(2500)
shark.move()

# Task: Create a scorpion class that inherits from monster. Health and energy from the parent. Add a poison_damage attribute. Overwrite the damage method to show poison damage 

class Scorpion(Monster):
    def __init__(self, scorpion_health, scorpion_energy, poison_damage):
        super().__init__(health = scorpion_health, energy = scorpion_energy)
        self.poison_damage = poison_damage

    def attack(self):
        print(f"Scorpion has dealt {self.poison_damage}!")

scorpion = Scorpion(poison_damage = 50, scorpion_health = 20, scorpion_energy = 10)
scorpion.attack()

print("health", scorpion.health)
print("energy", scorpion.energy)