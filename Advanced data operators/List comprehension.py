""" 
List comprehension = A way to create lists on a single line of code

"""
# Create a list with numbers from 0 to 99:
my_list = []
for num in range(0,100):
    my_list.append(num)
print("First method", my_list)

# With list comprehension:
my_list = []
my_list = [num for num in range(0, 100)]
print("Second method", my_list)

my_list = []
my_list = [(num, num * 2, num) for num in range(0, 100)]
print("With operations on data", my_list)

# You can also combine list comprehension with a ternary operator (This can be used to filter a list
# 1st way
my_list = []
my_list = [num for num in range(0, 100) if num < 10] # (Cannot use an else statement at the end of the if)
print("1st way", my_list)

# 2nd way
my_list = []
my_list = [num if num < 10 else 0 for num in range(0, 100)]
print("2nd way", my_list)

# Filtering a list
my_list_comp = [(num, num, num) for num in range(0, 100) if num < 50]
print("1st way", my_list_comp)

my_list_comp = [(num, num, num) if num < 20 else "no" for num in range(0, 100)]
print("2nd way" ,my_list_comp)

inventory_names = ["Screw", "Wheels", "Metal parts", "Rubber bits", "Screwdrivers", "Wood"]
inventory_numbers = [43, 12, 95, 421, 23, 43]
replenish_list = [(name, number) for name, number in zip(inventory_names, inventory_numbers) if number > 25] # Prints out the item if the number is greater than 25
print(replenish_list)


# Combine list comprehension
combined_comprehension = [[x for x in range(5)] for y in range(10)]
for row in combined_comprehension:
    print(row)
combined_comprehension = [[(x, y) for x in range(5)] for y in range(10)]
for row in combined_comprehension:
    print(row)


# Task: 
# Create the fields for a chess board

# My method
chess_board = [[(letter, y) for letter in ["A", "B", "C", "D", "E", "F", "G", "H"]] for y in range(9)]
for row in chess_board:
    print(row)
    

# Video method
chess_board = [[f'{letter}{num}' for num in range(1,9)] for letter in 'ABCDEFGH']
for row in chess_board:
    print(row)

# Making the board start from H to A
chess_board = [[f'{letter}{num}' for num in range(1,9)] for letter in 'ABCDEFGH'[::-1]]
for row in chess_board:
    print(row)
