""" Complex inheritance, for example could be one child class and two parent classes or more.
"""

class Monster:
    def __init__(self, health, energy, **kwargs): # **kwargs stores any arguments after health and energy in a dictionary. By using this, the Monster's super().__init__ must use keywords i.e. health = health, energy = energy
        print(kwargs)
        self.health = health
        self.energy = energy
        # Because the MRO goes from Shark --> Monster ---> Fish. This means that after Shark has inherited Monster, this super().__init__ will call Fish's init method
        super().__init__(**kwargs) # ** unpacks dictionaries. It turns each key:value pair in the dictionary into an argument. 

    def attack(self, amount):
        print("The monster has attacked!")
        print(f'{amount} damage was dealt')
        self.energy -= 20

    def move(self, speed):
        print(f'The monster now moves at a speed of {speed}.')

class Fish:
    def __init__(self, speed, has_scales):
        self.speed = speed
        self.has_scales = has_scales

    def swim(self):
        print(f"The fish is swimming at a speed of {self.speed}!")

class Shark(Monster, Fish): # Shark inherits from the parent classes: Monster and Fish
    def __init__(self, bite_strength, health, energy, speed, has_scales):
        self.bite_strength = bite_strength
        #super().__init__ would look at the first parent class that Shark inherits from i.e. Monster
        # Passing speed and has_scales to the Monster init method so that it can call the Fish init method
        super().__init__(health = health, energy = energy, speed = speed, has_scales = has_scales)

""" MRO = Method Resolution Order --> The order in which the parent's init methods are being called """
print(Shark.mro())
""" For this, it starts with Monster and then Fish. The MRO is determined by the order in which the parent classes were passed into the class
e.g. 
Shark(Monster, Fish) would mean that Shark inherits Monster, and then Fish
Shark(Fish, Monster) would mean that Shark inherits Fish, and then Monster
 """

shark = Shark(bite_strength = 500, health = 900, energy = 150, speed = 9999, has_scales = False)

print(shark.bite_strength, shark.health, shark.energy, shark.speed , shark.has_scales)