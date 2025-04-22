import modules

print(modules.add(5, 3))        # Output: 8
print(modules.subtract(9, 2))   # Output: 7

import calculator  # Importing our custom module

x = 10
y = 5

print("Addition:", calculator.add(x, y))
print("Subtraction:", calculator.subtract(x, y))
print("Multiplication:", calculator.multiply(x, y))
print("Division:", calculator.divide(x, y))


# Output:
# Addition: 15
# Subtraction: 5
# Multiplication: 50
# Division: 2.0


import calculator

def main():
    print("📟 Welcome to the Python Calculator!")
    print("Available operations: add, subtract, multiply, divide")
    
    while True:
        op = input("\nEnter operation (or 'exit' to quit): ").lower()

        if op == 'exit':
            print("👋 Exiting the calculator. Goodbye!")
            break

        if op not in ['add', 'subtract', 'multiply', 'divide']:
            print("❌ Invalid operation. Try again.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("⚠️ Please enter valid numbers.")
            continue

        if op == 'add':
            result = calculator.add(num1, num2)
        elif op == 'subtract':
            result = calculator.subtract(num1, num2)
        elif op == 'multiply':
            result = calculator.multiply(num1, num2)
        elif op == 'divide':
            result = calculator.divide(num1, num2)

        print(f"✅ Result: {result}")

if __name__ == "__main__":
    main()