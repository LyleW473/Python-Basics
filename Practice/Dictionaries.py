"""
Questions are from:
https://pynative.com/python-dictionary-exercise-with-solutions/
"""

# Exercise 1: Convert two lists into a dictionary
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

key_values = list(zip(keys, values))

dictionary = {}

for key, value in key_values:
    dictionary[key] = value

print(dictionary)


# Exercise 2: Merge two Python dictionaries into one
dict1 = {'Ten' : 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict3 = dict1.copy()
dict3.update(dict2)
print(dict3)


# Exercise 3: Print the value of key 'history' from the below dict
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
# 1st method
print(sampleDict.get("class").get("student").get("marks").get("history"))

# 2nd method
print(sampleDict["class"]["student"]["marks"]["history"])


# Exercise 4: Initialize a dictionary with default values
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

dictionary = dict.fromkeys(employees, defaults)
print(dictionary)


# Exercise 5: Create a dictionary by extracting the keys from a given dictionary
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

new_dict = {}

for key in keys:
    if key in sample_dict.keys():
        new_dict[key] = sample_dict.get(key)

print(new_dict)

# With dictionary comprehension
new_dict2 = {key: sample_dict.get(key) for key in keys}
print(new_dict2)


# Exercise 6: Delete a list of keys from a dictionary
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to remove
keys = ["name", "salary"]

# My method:
[sample_dict.pop(key) for key in keys]
print(sample_dict)

# Website method
sample_dict = {k: sample_dict[k] for k in sample_dict.keys() - keys}
print(sample_dict)


# Exercise 7: Check if a value exists in a dictionary
sample_dict = {'a': 100, 'b': 200, 'c': 300}
# 1st method
for value in sample_dict.values():
    if value == 200:
        print(f'{value} exists in this dictionary')

# 2nd method
if value == 200 in sample_dict.values():
    print(f'{value} exists in this dictionary')


# Exercise 8: Rename key of a dictionary
sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
sample_dict["Location"] = sample_dict.pop("city")
print(sample_dict)


# Exercise 9: Get the key of a minimum value from the following dictionary
sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}
# 1st method
for key in sample_dict.keys():
    if min(sample_dict.values()) == sample_dict[key]:
        print(key)

# With dict comprehension
value = {key for key in sample_dict.keys() if min(sample_dict.values()) == sample_dict[key]}
print(value)

# Website method:
print(min(sample_dict, key=sample_dict.get))


# Exercise 10: Change the value of a key in a nested dictionary
sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}

sample_dict["emp3"]["salary"] = 8500
print(sample_dict)