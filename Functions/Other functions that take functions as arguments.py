"""
(Map and filter have been replaced by list comprehension)

Map - changes values with a function inside a iterable

Filter - Filters out values from a condition

"""

# Map

my_list = [1,2,3,4,5]

# Creating function
def power_function(num):
    return num ** 2

print(list(map(power_function, my_list)))

# With lambda function
print(list(map(lambda num: num ** 2, my_list)))

# Filter 

# Creating a function
def get_below_4(num):
    """ True or False determines whether the item stays inside the list or not"""
    if num < 4:
        return True
    else:
        False   


print(list(filter(get_below_4, my_list)))

# With lambda function 
print(list(filter(lambda num: num < 4, my_list)))


# Task: Convert the power function and the filter one to list comprehension

# Power function
print([num **2 for num in my_list])

# Filter function 
print([num for num in my_list if num < 4])
