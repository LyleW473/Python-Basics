# Dictionary comprehension
dict_comprehension = {num: num ** 2 for num in range(25)} # {key:value, key for key in range(?)}
print(dict_comprehension)

# Set comprehension
set_comprehension = {num for num in range(100)}
print(set_comprehension)

# Tuple comprehension
tuple_comprehension = tuple(num for num in range(10))
print(tuple_comprehension)

# Task:

"""
- Create a dictionary with the keys 'A', 'B', 'C', 'D' and 'E'
- Each key should have a list as value with the values [1,2,3,4,5]
"""

task_dict_comprehension = {letter: [1,2,3,4,5] for letter in 'ABCDE'} 
print(task_dict_comprehension)