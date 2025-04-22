# 🌟 Exception Handling with try, except, else, and finally in Python
# Exception handling allows a program to deal with unexpected situations (errors) without crashing. Python provides a powerful structure to catch and handle these errors using:

# try

# except

# else

# finally

# ✅ try Block
# The try block contains code that might raise an exception.

# ❌ except Block
# The except block runs if an error occurs in the try block.

# ✨ else Block
# The else block runs if no error occurs in the try block.

# 🔒 finally Block
# The finally block always runs, whether an exception occurred or not — often used for cleanup actions.


# 📌 Example 1: Basic Try-Except
try:
    number = int(input("Enter a number: "))
    print("You entered:", number)
except ValueError:
    print("Oops! That's not a valid number.")

# What’s happening?
# If the user enters something that’s not a number, the except block catches the ValueError.

# 📌 Example 2: Try-Except-Else
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid input!")
else:
    print("Great! You entered:", number)

# Why use else?

# The else block is useful if you want to run some code only if no exception was raised.


# 📌 Example 3: Try-Except-Finally
try:
    f = open("data.txt", "r")
    content = f.read()
    print(content)
except FileNotFoundError:
    print("The file does not exist.")
finally:
    print("Closing file (if it was opened).")
    try:
        f.close()
    except:
        pass

# What’s happening here?

# If the file doesn’t exist, the except block handles it.

# Regardless of what happens, the finally block runs and attempts to close the file.

# 📌 Example 4: Full Try-Except-Else-Finally Structure
try:
    num1 = int(input("Enter numerator: "))
    num2 = int(input("Enter denominator: "))
    result = num1 / num2
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Invalid input. Please enter numbers only.")
else:
    print("Result is:", result)
finally:
    print("Execution completed.")



    