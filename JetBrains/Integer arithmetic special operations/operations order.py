# Python Lesson: Understanding the Order of Operations (PEMDAS)

# Introduction
"""
This lesson demonstrates the order of operations in Python using a complex arithmetic expression.
The order of operations, also known as operator precedence, dictates the sequence in which operations are evaluated in an expression. This concept is crucial for writing correct and predictable code.
"""
# Example expression to demonstrate oder of operations
# The expression below includes addition, subtraction, exponentiation, and divisio
# According to PEMDAS, the operations will be executed in the following order:
# 1.Exponantion (**)
# 2.Division (/)
# 3.Addition (+)
# 4.Subtraction (-)
result = (5 + 3) - 6**2 / 3

# Print the result with a descriptive message
print("The result of the expression (5 + 3) - 6**2 / 3 is:", result)

# Function to demonstrate order of operations with different inputs
def complex_expression(a, b, c):
    """Calculate the result of the expression (a + b) - c**2 / b
    
    Args:
    a (int): First number in the expression
    b (int): Second number in the expression
    c (int): Third number in the expression

    Returns:
    float: Result of the complex expression
    """
    # The expression is evaluated using the order of operations:
    # 1. Parentheses (a + b)
    # 2. Exponentiation (c**2)
    # 3. Division (/ b)
    # 4. Subtraction (-)
    return (a + b) - c**2 / b

# Define the variables
a = 5
b = 3
c = 6

# Test the function with example inputs
test_result = complex_expression(a, b, c)
print(f"The result of the function complex_expression({a}, {b}, {c}) is:", test_result)

# Detailed Explanation:
"""
In Python, the order of operations follows the PEMDAS rule:
P = Parentheses: Operations inside parentheses are performed first.
E = Exponents: Exponential calculations (e.g., 2**3) are performed next.
M = Multiplication and D = Division: These operations are performed from left to right.
A = Addition and S = Subtraction: These operations are peformed from left to right.

In the expression (5 + 3) - 6**2 / 3:
1. The parentheses are evaluated first, so the result of (5 + 3) is 8
2. Exponent: 6**2 = 36
3. Division: 36 / 3 = 12.0
4. Subtraction: 8 - 12.0 = -4.0

Therefore, the result of the expression (5 + 3) - 6**2 / 3 is -4.0.
"""

# Story Integration:
"""
Charles, the young hero in the magical land of Operator Order, must solve an arithmetic problem to return home.
With the help of the Wizard of Order and the ancient book of the Pythonista , Charles learns the PEMDAS rule.
By understanding and applying this rule, Charles successfully builds a magical bridge and returns home, 
earning the title 'Wizard of Pythonista' for his newfound knowledge and skill.
"""