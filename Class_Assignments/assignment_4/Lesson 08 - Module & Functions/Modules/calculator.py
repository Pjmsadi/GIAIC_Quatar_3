# This is a simple calculator module that provides basic arithmetic operations.
# It includes functions for addition, subtraction, multiplication, and division.

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Divide by zero"
    return a / b