""" Slicing to pick multiple elements from a list
- [1, 2, 3, 4,][start:end:step], The default values for step is 1.
- Python only goes up to the end index but does not include it. For example [1, 2, 3, 4] [1:2] would only get return one number
- List slicing returns a list.
- You can also include a third number for the direction / step. By default it is always 1 , meaning we increase the index by 1

"""
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_list[1:2]) # Would return the 2nd element inside the list, but not the third 
print(my_list[0:3]) # Would return all the elements up to ,but not including, the 4th element

# Slicing using directions / step , the 3rd number is to declare the direction / step
print(my_list[0:8:2]) # Returns values from element 0 to 8, with step 2. So it will return Elements, 0, 2, 4, 6
print(my_list[8:0:-1]) # Returns values from element 8 to 0 in reverse order with step -1
print(my_list[-1:4:-1]) # Starts from index -1, which is "10", and returns all the elements up to but not including the 5th element, with step -1.

# Negative slicing
print(my_list[::2]) # The default values will always be (0th index, last index, 1), so even if we don't mention it, this will still return the values in the list with step 2.
print(my_list[::-1]) # This would return all items in the list in reverse order. It does this by iterating over all the elements of the list, but backwards.


# Tuple slicing
my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(my_tuple[0:5:3]) # Would return the the first and 3rd element (from elements 0 to 5), because of step 3.

# Task: Start from 8 and go to 2, pick every second element
print(my_list[7:0:-2])

print(my_list[-3:0:-2])



