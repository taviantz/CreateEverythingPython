# Complex Expressions in Python

# Example expression to demonstrate order of operations
# According to the order of operations (PEMDAS/BODMAS):
# 1. Parentheses ()
# 2. Exponentiation **
# 3. Multiplication *, Division /, Integer Division //, Modulo %
# 4. Addition +, Subtraction -

# Calculate the result of the expression (5 + 3) - 6**2 / 3
# Step-by-step breakdown:
# 1. Parentheses: (5 + 3) = 8
# 2. Exponentiation: 6**2 = 36
# 3. Division: 36 / 3 = 12.0
# 4. Subtraction: 8 - 12.0 = -4.0

result = (5 + 3) - 6**2 / 3

# Print the result
print("The result of the expression (5 + 3) - 6**2 / 3 is:", result)