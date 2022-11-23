# List unpacking
def print_all(first ,*arguments, extra):
    print("first = ", first)
    print("arguments = ", arguments)
    print("extra = ", extra)
    # Print all arguments
    for argument in arguments:
        print(argument)

print_all(1,2,3,4,5, "hello", 1, 3, 215,5412,65312,62,12,88, extra = 2831920)

# Keyword unpacking, dictionaries
def print_more(**arguments):
    print(arguments)

print_more(arg1 = "1", arg2 = "test", arg3 = [1,2,3])

def print_even_more(*arguments, **keywordarguments):
    print(arguments)
    print(keywordarguments)

print_even_more(1,2,3,4,64,1,31,"hello", True, False)
print("------------")
print_even_more(1,2,3,4,64,1,31,"hello", True, False, test = 1, test2 = 2)

# Task: Create a calculator function that prints out the sum of an unlimited amount of numbers

def print_sum(*arguments):
    sum = 0
    for argument in arguments:
        sum += argument
    print(sum)


# Other method:
def calculator(*arguments):
    print(sum(arguments))

print_sum(1,23814,318,38,9965,281,594,931,58,6,8,18,593,193,594,43,8,12,9123,9,1,4,46,2,1,7,213,7,23,89,125134,7125,812,31723,123,72,31,7)

calculator(1,23814,318,38,9965,281,594,931,58,6,8,18,593,193,594,43,8,12,9123,9,1,4,46,2,1,7,213,7,23,89,125134,7125,812,31723,123,72,31,7)