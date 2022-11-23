""" 
- Lambda functions are single line functions
- The result is automatically returned

Uses:
- Some functions want other functions as arguments e.g. sort([1,5,2,3,4], function)
- Graphical user interfaces
"""

a = lambda x: x + 1
print(a(15))


simple_calculator = lambda a,b: a + b
print(simple_calculator(5, 25))

# Task: 
"""
- Create a lambda function that accepts 1 integer argument
- If the integer is > 5 return  hello
- Otherwise return bye
"""

task_function = lambda x: "Hello" if x > 5 else "Bye"

print(task_function(6))

# Documenting functions (explaining what a function does) 

def test(a : int = 10, b: int = 0) -> int: # I am declaring "a" as an integer and the default value is set to 10, the "->" is to indicate what is being returned from the function (it can be any datatype e.g. list)
    """ A simple function that prints 2 parameters """  # This is called a docstring
    print(a, b)

    return a + b

test(1,2)
print(test.__doc__) # Print the docstring
help(test) # Does the same thing