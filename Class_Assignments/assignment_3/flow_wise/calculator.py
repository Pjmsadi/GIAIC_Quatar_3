# ======================================
# Simple Calculator Program
# ======================================

# ------------------
# User Input Section
# ------------------
operation: str = input("Enter arithmetic operation (+, -, *, /): ")
num1: float = float(input("Enter first number: "))
num2: float = float(input("Enter second number: "))

# ------------------
# Calculation Section
# ------------------
result: float | str  # Union type for numeric or error message

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 == 0:
        result = "Error! Division by zero is not allowed"
    else:
        result = num1 / num2
else:
    result = f"Error! Invalid operation '{operation}' - please use +, -, *, or /"

# ------------------
# Result Presentation
# ------------------
print("\nCalculation Summary:")
print(f"  {num1} {operation} {num2} = ", end="")

if isinstance(result, float):
    # Format numeric output to 2 decimal places
    print(f"{result:.2f}")
else:
    # Display error message in red (if terminal supports it)
    print(f"\033[91m{result}\033[0m")