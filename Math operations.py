x = 10

# Power
print(x ** 2)

# Divide
print(x / 5)
# Floor division
print(x // 5)  # Truncates the result (cuts off anything after the decimal point)

# MOD
print(x % 2)

# Comparison operators
print(10 > 5)

print(10 < 5)

# Task: Find mean of numbers from 1 to 7
total = 0
num_of_i = 0
for i in range(1,8):
    num_of_i += 1
    total += i

mean = (total / num_of_i)
print("mean = ", mean)