def add(a, b):
    return a + b

class Test:
    def __init__(self, add_function):
        self.add_function = add_function
        

test = Test(add_function = add)
print(test.add_function(50, 5))

# Task: Create a Monster class with a parameter called func, store this func as a parameter
# Create another class, called Attacks, that has 4 methods: bite, strike, slash, kick (each method just prints some text)




class Monster:
    def __init__(self, func):
        self.func = func



class Attacks:
    def bite(self):
        return "BITE!"

    def strike(self):
        return "STRIKE!"

    def slash(self):
        return "SLASH"
    
    def kick(self):
        return "KICK"

monster = Monster(func = Attacks().bite) # Attacks() creates an object of the Attacks. Without the two brackets, the entire class would be passed in.
print(monster.func())
"""
This is the same as: 
attacks = Attacks()
monster = Monster(func = attacks.bite) 

"""