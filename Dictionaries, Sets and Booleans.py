
# Dictionaries
""" These are complex containers for other variables 
    {"key" : "value", 1: [1,2,3]}

- Dictionaries store data but things are more organised since each value has a key
- Indexing does not work with dictionaries

"""

# Creating a dictionary

my_dictionary = {"Lyle": 123, "B" : [4,5,6], "C" : True}
print(my_dictionary)

my_dictionary_2 = {"Lyle": 123, "B" : [4,5,6], "C" : True , "B" : "Replaced"} # Declaring another key:value pair will override the previous one if it shares the same key name
print(my_dictionary_2)

# Creates a dictionary using the specified keys and values
x = ("Key 1", "Key2", "Key3")
y = 0 

my_dictionary_3 = dict.fromkeys(x,y)
print(my_dictionary_3)


# Returning all values in the dictionary
print(my_dictionary.values())

# Returns a list containing the dictionary's keys
print(my_dictionary.keys())

# Return the value of a specified key
print(my_dictionary.get("Lyle"))

# Return a list containing a tuple for each key value pair
print(my_dictionary_2.items())


# Removes all elements from a dictionary
print(my_dictionary_2.clear())

# Returns a copy of the dictionary
my_dictionary_2 = my_dictionary.copy() # Here I assigned the second dictionary to be a copy of the first dictionary
print(my_dictionary_2)

# Remove the element with the specified key
print(my_dictionary)
my_dictionary.pop("Lyle")
print(my_dictionary)

# Remove the last inserted key-value pair
print(my_dictionary_2)
my_dictionary_2.popitem()
print(my_dictionary_2)

# Update the dictionary with specified key-value pairs
my_dictionary_2.update({"Lyle": 789})
my_dictionary_2.update({"Jeff" : 'Hello'}) # If there isn't a Key called "Bob", it creates a new key:value pair and adds it to the dictionary
print(my_dictionary_2)

# Returns the value of a specified key. If the key doesn't exist then it inserts the key with the specified value
x = my_dictionary_2.setdefault("Lyle")
print(x)

my_dictionary_2.setdefault("Bobby", 'goodbye') # Second parameter is the specified value 
print(my_dictionary_2)

my_dictionary_2.setdefault("Grace") # Without a second parameter being passed in, the default value becomes "None"
print(my_dictionary_2)

# Converting a dictionary into a list
print(list(my_dictionary_2)) # A list with all the keys

# Converting a dictionary into a string
print(str(my_dictionary_2)) # A list with all the keys and values as strings

# Ways of getting values from dictionaries
my_dictionary_3 = {"Poppy": 456, "B" : [4,5,6]}

print(my_dictionary_3.get("Poppy")) # This is more sensible because if the key "Poppy" did not exist, it would cause an error if you used the 2nd method below
print(my_dictionary_3["Poppy"])
# print(my_dictionary_3["X"]) This would cause an error because a key "X" does not exist in my_dictionary_3


# Task: Use the update method to add another key value pair
print(my_dictionary_3)

my_dictionary_3.update({"Poppy": 32929320}) # Overrides the last value for Poppy
my_dictionary_3.update({"Yuta": "Hello"}) # Creates a new key:value pair
print(my_dictionary_3)

my_dictionary_3.update(D = "Test") # Another way of using the update method which creates a new key:value pair
print(my_dictionary_3)

my_dictionary_3.update(E = "Bye", F = 2392392, G = "sl2392") # You can use this method to create multiple new key:value pairs
print(my_dictionary_3)

my_dictionary_3["H"] = 238775
print(my_dictionary_3)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Sets
""" These are simple containers for other variables

{1, "Test", True}

- It is like a dictionary, except it has no keys
- Each value ina  set must be unique, and duplicates are deleted
- Indexing and slicing does not work with sets
- Useful for making comparisons between sets

"""
# Creating a set
my_set = {1,2,3,4}
print(my_set)

# Duplicate values are deleted
my_set_2 = {1,2,3,4,5,5,6,6} 
print(my_set_2) 

# Adding to a set
my_set.add(5) # Adds the value 5 to the set
print(my_set)

# Removing from a set
my_set.remove(3) # Removes the value 3 from the set
print(my_set)

# Removing all elements from the set
my_set_2.clear()
print(my_set_2)

# Returning a copy of the set
my_set_2 = my_set.copy()
print(my_set_2)

# Getting values from a set
print(my_set_2.pop()) # Pops the first item off the set
print(my_set_2)


# Task: Use type conversion to get one item from the set by index
x = list(my_set)
print(x)
print(x[0]) # First item in the set
print(x[::-1]) # All items in the set in reverse order

print(list(my_set)[3])

# Comparing between sets
set1 = {1,2,3,4,4}
set2 = {4,5,6,7}

# Returns a set which contains all the items from the original set
x = set1.union(set2)
print(x)

x = set1 | set2  # Performs the same operation
print(x) 

# Returns a set which contains the items that exist in both set x and y. Since "4" is in set1 and set2, y = {4}
y = set1.intersection(set2)
print(y)

y = set1 & set2  # Performs the same operation
print(y)

# Returns a set that contains the difference between two sets. The returned set contains items that only exist in the first set, not both of the sets
z = set1.difference(set2)
print(z)

k = set2.difference(set1)
print(k)

z = set1 - set2 # Performs the same operation 
print(z)

k = set2 - set1 # Performs the same operation
print(k)

# Task: Check if the list has duplicate values
test_list = [43,25,223,232,5,75,545,43,423,7,68,9,534,32,3232,575,42,5,6,2,62,19,23,62,612,23,78]

# My method, this returns the duplicate value as well
x = set(test_list[0:(len(test_list) - 1) // 2])
print(x)
y = set(test_list[len(test_list) // 2 : len(test_list)])
print(y)

intersections = x.intersection(y)
print(intersections)

# Video method
print(len(test_list))
print(len(set(test_list)))
print(len(test_list) == len(set(test_list))) # Returns a Boolean value to if there were duplicate values. False means that there were duplicate values

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Booleans
""" 
- Usually created from comparison operators
- They can also be created in many other ways e.g. Strings with methods that return booleans, checking if values are in lists, comparing sets, etc.

== : equal
!= : not equal
< : smaller than
<= : smaller or equal than
> : greater than
>= : greater or equal than

- "not" reverses a Boolean

"""

print(1 == 10) # True if equal
print(1 != 10) # True if it is different
print(10 < 10) # Returns False

# Booleans and lists and strings
print(1 in [1,2,3]) # Returns True
print("e" in "hello") # Returns True
print("x" in "hello") # Returns False

print(4 not in [1,2,3]) # Returns True as 4 is not in the list

# Booleans by themselves
print(True)
print(not True)
print(False)
print(not False)

# Task: Check if the key 1 exists in the dictionary, check if the value four exists in the dictionary

dictionary = {1:"one", 2: "two", 3: "three"}

print(1 in dictionary.keys()) # The key "1" is in the dictionary so returns True
print("four" in dictionary.values()) # The value "four" is not in the dictionary so returns False



# bool() function 
"""" 
- Accepts any number, string, type of container and still returns a value
- Truthy - values that are converted to True
- Falsy - values that are converted to False

Values that are "Falsy":
- 0 or 0.0 (int or float)
- " (empty string)
- [], (), {} (empty list, tuple, set or dictionary)
- None (absence of a value)

Anything else is "Truthy"
"""

print(bool(2382382832832)) # As it is a number that isn't zero, it is True
print(bool(0)) # Returns False
print(bool(None))


# Other datatypes

""" 
 Functions to change datatypes:
- int()
- float()
- str()
- bool()
- list()
- dict()
- tuple()
- set()

Other datatypes include:
- None = absence of a value
- Sequence = To get a range of numbers

More specific types of data for highly specific purposes:
- Bytes
- Complex numbers
- Memoryview
- Frozensets

"""

