# Print the largest value in an iterable or the largest out of two or more arguments
print(max(1,6,10,2,))
# Print the smallest value in an iterable or the largest out of two or more arguments
print(min(1,6,10,2))


test = 'Hello World'.upper()  # Convert a word into uppercase or lower case
print(test)

username = "JoJSUqnsmiQ Jskqlao"
print(username.upper())
print(username.lower())
print(username.title()) # Ensures that the first letter in a word is uppercase and the rest of them are lowercase
print(username.strip('J')) # Removes the letter that is passed in as a parameter into the 'strip' method. 

print(dir(username)) # Can check the methods available to "username" variable.

username = "sdlaqodlssodwqo"
print(username.isalpha()) # Print True or False depending on if all the letters in the word are in the alphabet or not. (Spaces or numbers are not in the alphabet so would return False))


test_variable = 'A word'.upper().replace('A', 'X') # Changes all letters inside of the string into uppercase. The replace method then replaces all letters 'A' with the letter 'X'
print(test_variable)


# Task: Replace the word "puppies" with a different word

exercise_string = 'I like puppies'
print(exercise_string.replace('puppies', 'cats'))

exercise_string = 'I like puppies puppies puppies'
print(exercise_string.replace('puppies','cats', 2)) # Last parameter declares how many times I want to replace 'puppies' with 'cats'
