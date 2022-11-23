""" 
A matchcase is similar to an if statement.
- It runs code if a condition is True
- Match case is better to check for one value out of a long list

if 'hungry':
    code
elif 'tired':
    code

elif 'bored':
    code

is the same as: (It has better readability)

match mood:
    case 'hungry':
        code
    case 'tired':
        code
    case 'bored':
        code

"""


mood = "bored"

match mood:
    case "hungry":
        print("Get some food")
    case "thirsty":
        print("Get some water")
    case "tired":
        print("Get some sleep")

    case _: # Acts like the else statement, this refers to anything that isn't the cases above
        print("Any other mood", mood)

""" Task: 
- Create a variable with an integer between 1 and 5 and call it grade.
- Create a match case statement that writes "very good" when the grade is 1 
- Create a match case statement that writes "very bad" when the grade is 5 (and all other cases between)
# There should be some default behaviour if you get an unexpected value
"""

grade = 9

match grade:
    case 1:
        print("Very good")
    case 2:
        print("Good")
    case 3:
        print("Okay")
    case 4:
        print("Needs improvement")
    case 5:
        print("Very bad")
    case _:
        print("Invalid grade")

    