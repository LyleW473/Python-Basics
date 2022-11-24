""" 
Python can delete things using "del"
"""

# Remove items from a list by index

my_list = [23,55,65,8]

del(my_list[2])

print(my_list)

my_list = [23,55,65,8]
my_list.pop(-1)
print(my_list)

# Remove an item by value
my_list = [23,55,65,8]
my_list.remove(23)
print(my_list)

# Clear the entire list
my_list = [23,55,65,8]
my_list.clear()
print(my_list)