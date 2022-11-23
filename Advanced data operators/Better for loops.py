inventory_names = ["Screw", "Wheels", "Metal parts", "Rubber bits", "Screwdrivers", "Wood"]
inventory_numbers = [43, 12, 95, 421, 23, 43]

# Loop over both lists simultaneously
print(list(zip(inventory_names, inventory_numbers)))


for name, number in zip(inventory_names, inventory_numbers): # Whenever Python sees a tuple, it will assign the first item to the name variable, and the second item will be assingned to number
    print(f'{name} current inventory: {number}')


# Enumerate function - Get the current index of the function
print(list(enumerate(inventory_names))) # Insert an iterable


for pair in enumerate(inventory_names):
    print(pair)

for index, name in enumerate(inventory_names):
    print(f'{index}: {name}')
    if index == len(inventory_names) // 2:
        print("Halfway complete")
 
# Task: Combine zip and enumerate to get 'Screws [id: 0] - inventory: 43'
data = list(zip(inventory_names, inventory_numbers))

print(data)

for index, inventory_tuple in enumerate(zip(inventory_names,inventory_numbers)):
    print(f'{inventory_tuple[0]} [id: {index}] - inventory: {inventory_tuple[1]}')
