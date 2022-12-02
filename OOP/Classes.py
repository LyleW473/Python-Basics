class Monster:
    # Attributes
    health = 90
    energy = 40

    # Methods
    def attack(self, amount):
        print("The monster has attacked!")
        print(f'{amount} damage was dealt')

    def move(self, speed):
        print(f'The monster now moves at a speed of {speed}.')


monster = Monster()
print(monster.health, monster.energy)
monster.attack(932913123120)
monster.move(20000)