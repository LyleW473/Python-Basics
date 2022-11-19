''' 
Strings = 'words'
Integer = 123  Whole numbers
Float = 1.23  Floating point numbers
Boolean = True/False

List = [1,2,'test']  A list can have different types of data types and can be changed
Tuples = (1,2,'test') A tuple is similar to a list but it cannot be changed
Set = {1,2, 'test'} A set is used to store multiple items in a  single variable. They do not allow duplicate values. Items in a set cannot be changed. Every value within a set must be unique
Dictionaries = {'a' : 1, 'b':'hello'} Used to store data values in "key:value" pairs

'''
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Numbers

# Find the datatype of something
print(type(1))
print(type(2.2))
print(type('Hello'))
print(type(1.1 + 1)) # Adding a float with an integer will automatically convert it into a float

# Converting between floats and integers
print(float(2))
print(int(5.9)) # Truncates 5.9, it doesn't round it

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Strings
''' 
- You can declare a string using " or '   
- You can also use strings with math operations i.e. "hello" + "world"

'''

test_variable = 'Test 1'
test_variable_2 = "Test 2"
print(test_variable, test_variable_2)

# Quotes inside of strings
test_variable_3 = "He said 'This was great'"
print(test_variable_3)

test_variable_4 = '\"' # Escape character \ is used in front of the letter you want Python to interpret as a normal character
print(test_variable_4)

# Escape characters
test_variable_5 = 'Line 1: some text line \nLine 2: some more text' # \n tells Python to add a line break between the string
print(test_variable_5)
test_variable_5 = 'Line 1: some text line \tLine 2: some more text' # \t tells Python to add a tab between the string
print(test_variable_5)
test_variable_5 = 'Line 1: some text line \tLine 2: some more text' # \r is another line break

# Writing multiple lines, by assigning to a variable
test_variable_6 = ''' A comment
write some more text
write more text '''
print(test_variable_6)

# Math and strings
test_variable_7 = 'hello' +' ' + 'world'
print(test_variable_7)
test_variable_7 = 'copy' * 10
print(test_variable_7)

# Getting values into strings
name = 'Bill'
age = 37
greeting_string = 'Hello {}, you are {} years old'.format(name, age) 
print(greeting_string)
greeting_string = 'Hello {one}, you are {two} years old'.format(one = name, two = age)
print(greeting_string)

greeting_string = f'Hello {name}, you are {age} years old'
print(greeting_string)

greeting_string = f'Hello {name}, you are {age + 10} years old'
print(greeting_string)

# Task: Create a string that states your name and your hobby. Separate the string into two lines (using \n or """ """)
name = 'Lyle'
hobby = 'coding'
greeting_string = f'Hello, my name is {name} \nand my hobby is {hobby}'
print(greeting_string)


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Lists and Tuples
# Main difference between the two is that tuples are immutable, they cannot be changed.

# Lists
my_list = [1,2,3,4.5, "word"]
print(my_list)
print(len(my_list)) # Prints length of list

my_list.reverse() # Reverses the elements of the list in place
print(my_list)

my_list.clear() # Removes all items from the list
print(my_list)

my_list.append("Hello")
print(my_list)

# Tuples
my_tuple = (1,2,3, 1.523, "Word", [7,8,9])
print(my_tuple)

# Picking elements from a tuple or a list (indexing and slicing). [Slicing will be on a separate file]. Indexing does not work on sets or dictionaries.
print(my_tuple[2]) # Prints 3rd item in the list 
print(my_tuple[-1]) # Prints last item in the list
print(my_tuple[-3]) # Prints the 3rd last item in the list, so this would be 1.523


# Task: Get the word / string 'Hello' 
exercise_list = ['first entry', [123,456,[0,'Greetings']], 'bye'] 
print(exercise_list[1][2][1])
print(exercise_list[-2][-1][-1])


# Unpacking
a,b = (10,5) # Assigns a to the first value of the tuple or list, assigns b to the second value of the tuple or list
print(a)
print(b)

c,d = [20,'Hello'] 
print(c)
print(d)
print(c,d)
# Unpacking allows you to easily assign multiple variables on a single line
e,f,g = 1,"Hello", 4.5
print(e)
print(f)
print(g)
print(e,f,g)

# Task: Switch the values of the two variables
value_1 = 10
value_2 = 'Test'

print(value_1)
print(value_2)

value_1, value_2 = value_2, value_1

print(value_1) 
print(value_2)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Strings, tuples and lists

my_string = "This is a test"
my_list = [1,2,3,4]

# Turning a string into a list/tuple
print(my_string.split()) # Separates the string where there is a space (by default)
print(my_string.split("t")) # Separates the string whenever "t" appears

# Convert one datatype into a list
print(list(my_string))
# Convert one datatype into a tuple
print(tuple(my_string))

# Turn a list/ tuple into a string
print(" ".join(["one", "two"])) # Adds " " (a space) in between the elements of the list
print(" ".join(["one", "two", "three", "four"]))


print("two".join(["one","three"])) # Adds "two" in between the elements of the list
print("two".join(["one","five","hello","bye"]))


print(str(my_list)) # Converts my list into a string
print(type(str(my_list)))  

# Indexing on strings
print(my_string[::-1]) # Prints the string in reverse order
print(my_string[0:4]) # Prints the string elements 0 to 3 (so 4 letters)

# Task: Remove all th items inside test_list to only get 1 2 3 4 
exercise = str(my_list).strip("[").strip("]") # Gets rid of the list brackets
print(exercise)

exercise = exercise.replace(","," ")   # Replaces the commas with a space
print(exercise)

# Another way to do it
exercise = str(my_list).strip("[").strip("]").replace(","," ") # Does the same thing but in a single line
print(exercise)


