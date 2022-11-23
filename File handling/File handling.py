# Open and close it manually
file = open('File handling/test.txt')
print(list(file))
file.close()

# Open and close it automatically
with open('File handling/test.txt') as file:
    #print(list(file))
    #print(file.read())
    for line in list(file):
        print(line)


# Write some file
with open('File handling/test.txt', 'a') as file: # 'a' = Append , 'r' = Read, 'w' = Write. The default value is 'r'. 'w' would overwrite everything inside of the text file
    file.write('\nWrite some more text')


# Task: Create a new text file and draw a tree in it

with open('File handling/tree.txt','w') as tree_file:
    tree_string = '''  
                       x 
                      xxx
                     xxxxx
                       x
                       x
                       x
                '''
    tree_file.write(tree_string)