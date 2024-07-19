# Define the greet function
def greet():
    print("Hello, World!")

# Invoke the greet function
greet()

# Define the multiply function
def multiply(a, b):
    return a * b

# Invoke the multiply function
result = multiply(2, 3)
print(result) # Output: 6

#Example of using built-in functions
number = "123"

# Finding the length of a string
print(len(number)) # Output: 3

# Converting types
integer = int(number) #123
float_number = float(number) # 123.0

# Using the sum function with converted numbers
my_sum = sum((integer, float_number))
print(my_sum) # Output: 246.0

# Rounding the sum
print(round(my_sum)) # Output: 246

# Finding the minimum and maximum
print(min(integer, float_number)) # Output: 123
print(type(max(integer, float_number, my_sum))) # Output: <class `float`>