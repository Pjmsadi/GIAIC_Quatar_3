# ================================================
# For Loop Demonstrations
# ================================================

# ------------------
# Basic Iteration
# ------------------
fruits_list: list[str] = ["apple", "cherry", "banana", "mango"]
print("Iterating through fruits:")
for fruit in fruits_list:
    print(f"- {fruit.capitalize()}")

# String iteration
username: str = "Georgetown"
print("\nLetters in username:")
for letter in username:
    print(f"Character: {letter}")

# ------------------
# For-Else Construct
# ------------------
numbers: list[int] = [1, 2, 3, 4, 5, 6, 7]

# Complete loop example
print("\nComplete loop execution:")
for num in numbers:
    print(f"Processing number: {num}")
else:
    print("✔️ Loop completed without interruptions")

# Broken loop example
print("\nInterrupted loop execution:")
for num in numbers:
    print(f"Processing number: {num}")
    if num == 3:
        print("🛑 Breaking loop early")
        break
else:
    print("This won't execute due to break statement")

# Search pattern example
print("\nNumber search example:")
target_number = 8
for num in numbers:
    if num == target_number:
        print(f"🎯 Found target number {target_number}")
        break
else:
    print(f"❌ Target number {target_number} not found in list")

# ------------------
# Range Function Usage
# ------------------
# Basic range
print("\nCounting 0-4:")
for i in range(5):
    print(f"Count: {i}")

# Stepped range
print("\nEven numbers between 2-10:")
for even in range(2, 11, 2):
    print(f"Even: {even}")

# Reverse counting
print("\nCountdown from 5:")
for i in range(5, 0, -1):
    print(f"T-{i}")

# ------------------
# Practical Applications
# ------------------
# Index-based iteration
print("\nFruits with indexes:")
for index, fruit in enumerate(fruits_list, start=1):
    print(f"{index}. {fruit}")

# Multiplication table
print("\nMultiplication table (5x5):")
for row in range(1, 6):
    for col in range(1, 6):
        print(f"{row*col:2}", end=" ")
    print()  # New line after each row

# ------------------
# Iteration Techniques
# ------------------
# Dictionary iteration
person: dict[str, str | int] = {"name": "Alice", "age": 30, "job": "Engineer"}
print("\nDictionary items:")
for key, value in person.items():
    print(f"{key}: {value}")

# Zipped iteration
names = ["Alice", "Bob", "Charlie"]
scores = [95, 87, 91]
print("\nZipped iteration:")
for name, score in zip(names, scores):
    print(f"{name}: {score}/100")