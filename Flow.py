"""
In "For" and "While" loops:
- break = Ends the entire while/for loop
- continue = Skips the current iteration of the loop
- pass = A placeholder for future code, it does nothing


"""

# While loops 
# Task: Create a list with only even values from 0 to 100
list = []
x = 0
while x <= 100:
    # Append x to list
    list.append(x)  
    # Increment x by 2
    x += 2

print(list)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# For loops

# Iterating over a string
basic_string = "One two three"
for letter in basic_string:
    letter = letter.lower()
    print(letter)

# Iterating over integers
for num in range(10, 51, 5): # Start, End, Step
    print(num)

# Iterating over a dictionary
basic_dict = {1: "one", 2: "two", 3: "three"}

# Values
for value in basic_dict.values():
    print(value)

# Keys
for key in basic_dict.keys():
    print(key)

# Items
for item in basic_dict.items(): # Returns a tuple as: (key, value)
    print(item)


# Iterating over a set
basic_set = {1, 5, 21}
for item in basic_set:
    print(item)

# Task:
practice_list = [[10,40,20,50], [2,42,10], [101,1,4]]
"""
- Use a for loop to only print the numbers below 50
- Skip values below 10
- End the entire loop if a value is above 100
"""

for list in practice_list:
    for item in list:
        if item < 10:
            continue
        elif item < 50:
            print(item)
        elif item > 100:
            break

# Flow and line breaks

"""
if x < 5:
    colour = "blue"
else: 
    colour = "red"

Is the same as: (Ternary operator)

colour = "blue" if x < 5 else "red"

- This is a readable and efficient way of creating single line if statements
"""

x = 6
colour = "blue" if x < 5 else "red"
print(colour)

# Using ternary operator with format
print(f" The colour is {'red' if x < 5 else 'blue'}")

a = ['red' if x < 5 else 'blue', 'yellow', 'green']
print(a)
print(a[0], a[1], a[2])
