class Monster:
    """ A monster that has some attributes"""
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy

        # Private attributes
        self._id = 5 # An underscore is an indication for other developers to not modify this value (It can actually be changed, but it is just an indication)


    def attack(self, amount):
        print("The monster has attacked!")
        print(f'{amount} damage was dealt')
        self.energy -= 20

    def move(self, speed):
        print(f'The monster now moves at a speed of {speed}.')


monster = Monster(20, 10)

print(monster._id)

# hasattr 

# Useful to check if an object has an attribute
if hasattr(monster, "health"): # hasattr(object, attribute)
    print(hasattr(monster, "health"))


setattr(monster, "weapon", "sword") # setattr(object, attribute, value)
print(monster.weapon)

# setattr

# Useful for creating multiple new attributes 

new_attributes = (["weapon", "Axe"], ["armor", "Shield"], ["potion", "Mana"])
for attr, value in new_attributes:
    setattr(monster, attr, value)

print(vars(monster)) # vars returns all the name:value pair mappings for all names defined in the local scope, or the optional object argument's scope along with their associated values

# doc

# Explains what an object does (in the """ comments """)
print(monster.__doc__)

# help displays useful information about the class e.g. attributes and methods
help(monster)