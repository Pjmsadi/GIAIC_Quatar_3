# ==================================================
# Basic Conditional Statements
# ==================================================

# ------------------
# Simple If Statement
# ------------------
# Execute code only if condition is True
number: int = 10
if number > 0:
    print("The number is positive")

# ------------------
# If-Else Statement
# ------------------
# Execute different code blocks for True/False conditions
negative_number: int = -5
if negative_number > 0:
    print("The number is positive")
else:
    print("The number is negative")

# ------------------
# Elif Statement
# ------------------
# Check multiple conditions sequentially
zero_number: int = 0
if zero_number > 0:
    print("The number is positive")
elif zero_number < 0:
    print("The number is negative")
else:
    print("The number is zero")


# ==================================================
# Logical Operators
# ==================================================
age: int = 25
is_student: bool = True

# ------------------
# AND Operator
# ------------------
# True only if both conditions are True
if age > 18 and is_student:
    print("You are eligible for a student discount")

# ------------------
# OR Operator
# ------------------
# True if at least one condition is True
if age < 12 or age > 60:
    print("You qualify for a special discount")

# ------------------
# NOT Operator
# ------------------
# Reverses the boolean value
if not is_student:
    print("You are not a student")


# ==================================================
# Nested Conditional Statements
# ==================================================
check_number: int = 10

if check_number > 0:
    if check_number % 2 == 0:
        print("The number is positive and even")
    else:
        print("The number is positive and odd")
else:
    print("The number is negative")

# ==================================================
# Practice Exapmple
# ==================================================