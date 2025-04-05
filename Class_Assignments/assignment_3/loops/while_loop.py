# ================================================
# While Loop Demonstrations
# ================================================

# ------------------
# Basic Counter
# ------------------
print("Basic Counter:")
counter: int = 1
while counter <= 5:
    print(f"Count: {counter}")
    counter += 1
print("Counter reached 5!\n")

# ------------------
# User-Controlled Loop
# ------------------
print("Number Doubler (type 'stop' to exit):")
total = 0
while True:
    user_input = input("Enter a number: ")
    
    if user_input.lower() == 'stop':
        print("Exiting program...")
        break
        
    try:
        number = float(user_input)
        total += number
        print(f"Current total: {total:.2f}")
    except ValueError:
        print("Invalid input! Please enter a number or 'stop'")

print(f"Final total: {total:.2f}\n")

# ------------------
# Conditional Exit
# ------------------
print("Temperature Check:")
current_temp = 25
while current_temp > 15:
    print(f"Current temperature: {current_temp}°C")
    current_temp -= 2
    if current_temp <= 15:
        print("Warning: Temperature approaching 15°C limit!\n")

# ------------------
# Validation Loop
# ------------------
print("Age Verification:")
valid_age = False
while not valid_age:
    age_input = input("Enter your age (18-120): ")
    
    if age_input.isdigit():
        age = int(age_input)
        if 18 <= age <= 120:
            valid_age = True
            print("Age accepted!")
        else:
            print("Age must be between 18 and 120")
    else:
        print("Please enter numbers only")

print("Access granted!\n")

# ------------------
# Complex Condition
# ------------------
print("Password Attempts:")
max_attempts = 3
attempts = 0
correct_password = "Secure123"

while attempts < max_attempts:
    password = input("Enter password: ")
    
    if password == correct_password:
        print("Access granted!")
        break
        
    attempts += 1
    remaining = max_attempts - attempts
    print(f"Invalid password! Attempts remaining: {remaining}")

else:
    print("Account locked! Too many failed attempts\n")

# ------------------
# Real-world Simulation
# ------------------
print("Coffee Machine Simulation:")
water_level = 1000  # ml
while water_level > 0:
    print(f"\nWater remaining: {water_level}ml")
    cup_size = input("Choose cup size (small/medium/large): ").lower()
    
    if cup_size == 'small':
        water_level -= 200
    elif cup_size == 'medium':
        water_level -= 300
    elif cup_size == 'large':
        water_level -= 400
    else:
        print("Invalid selection!")
        continue
        
    print("Dispensing coffee...")

print("\nAlert: Out of water! Please refill\n")