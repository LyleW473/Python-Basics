""" This is on functions that take functions as arguments"""


list1 = [4,2,3,1,5]

# Two ways to sort a list:
# 1st:
list1.sort()
print(list1)

# 2nd:

print(sorted(list1, reverse= True))
print(sorted(list1, reverse= False))

# Problem:

list2 = [('a', 3), ('b', 10), ('c', 6), ('d', 5)]
# print(sorted(list2) would not work

# Creating a function

def sort_function(item):
    return item[1] # Return the second item inside of the tuple

print(sorted(list2, key = sort_function)) # The sorted function passes each tuple inside the list into "sort_function". This would sort it by the 2nd item in the tuple


# Using lambda function

print(sorted(list2, key = lambda item: item[1]))  # item = parameter, item[1] is being returned.


# Task: 
""" 
- Sort this list by inventory numbers
- Sort the list by length of the inventory name
"""
inventory_names = ["Screw", "Wheels", "Metal parts", "Rubber bits", "Screwdrivers", "Wood"]
inventory_numbers = [43, 12, 95, 421, 23, 43]
combined_list = list(zip(inventory_names, inventory_numbers))

# Sort by inventory numbers
sorted_comprehension_num = sorted(combined_list, key = lambda inventory_tuple: inventory_tuple[1])
print(sorted_comprehension_num)

# Sort by length of inventory name
sorted_comprehension_name = sorted(combined_list, key = lambda inventory_tuple: len(inventory_tuple[0]))
print(sorted_comprehension_name)