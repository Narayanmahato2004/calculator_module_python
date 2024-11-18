# calculator.py

# Add two numbers
def add(x, y):
    return x + y

# Subtract two numbers
def subtract(x, y):
    return x - y

# Multiply two numbers
def multiply(x, y):
    return x * y

# Divide two numbers
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Power function
def power(x, y):
    return x ** y

# Square root function
def sqrt(x):
    if x < 0:
        return "Error! Negative value for square root."
    return x ** 0.5
