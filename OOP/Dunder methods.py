""" Dunder methods refer to double underscore methods.   __Dunder__ methods   

A dunder method is a method taht is not called by the user, but is called by Python when something happens:

__init__ = called when the object is created
__len__ = called when the object is passed into len()
__abs__ = called when the object is passed into abs()

"""

class Monster:

    # Constructor
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy
        print(f"The monster was created with {self.health} HP and {self.energy} energy!")
    
    # Other methods
    def __len__(self):
        return self.health

    def __abs__(self):
        return self.energy

    def __call__(self):
        return ("The monster was called")
    
    def __add__(self, number):
        return self.health + number

    def __str__(self):
        return 'A monster'

    def attack(self, amount):
        print("The monster has attacked!")
        print(f'{amount} damage was dealt')

    def move(self, speed):
        print(f'The monster now moves at a speed of {speed}.')


monster = Monster(1000, 50)
monster.attack(932913123120)
monster.move(20000)
monster2 = Monster(250, 25)

print(len(monster)) # __len__
print(abs(monster)) # __abs__
print(dir(monster))
print(monster.__dict__) # __dict__
print(monster()) # __call__
print(monster + 20) # __add__
print(monster) # __str__