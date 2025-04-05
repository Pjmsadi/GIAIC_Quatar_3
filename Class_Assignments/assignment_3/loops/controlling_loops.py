# ================================================
# Loop Control Statements: break and continue
# ================================================

# ------------------
# Break Statement (Immediate Exit)
# ------------------
print("Searching for secret code (break example):")
codes = [112, 234, 355, 412, 567]
secret_code = 412

for code in codes:
    print(f"Checking code: {code}")
    if code == secret_code:
        print("🔑 Secret code found! Access granted.")
        break
print("Search complete!\n")

# ------------------
# Continue Statement (Skip Iteration)
# ------------------
print("Processing valid transactions (continue example):")
transactions = [150, -50, 300, -20, 0, 450]

for amount in transactions:
    if amount <= 0:  # Skip invalid transactions
        continue
    print(f"✅ Processing valid transaction: ${amount}")
print("Transaction batch completed!\n")

# ------------------
# Practical Combination Example
# ------------------
print("Temperature Monitoring System:")
readings = [22.5, 25.1, 30.0, 18.7, 45.3, 28.9]
MAX_TEMP = 40.0

for temp in readings:
    if temp > MAX_TEMP:
        print(f"🚨 Critical temperature {temp}°C detected! Shutting down.")
        break
    if temp < 20.0:
        print(f"⚠️  Low temperature warning: {temp}°C (skipping processing)")
        continue
    print(f"🌡 Processing normal reading: {temp}°C")
print("Monitoring cycle finished.\n")

# ------------------
# Nested Loop Control
# ------------------
print("Matrix Search (nested loops):")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
target = 5

for row_idx, row in enumerate(matrix):
    for col_idx, value in enumerate(row):
        print(f"Checking position ({row_idx},{col_idx}) = {value}")
        if value == target:
            print("🎯 Target found!")
            break  # Only exits inner loop
    else:
        continue  # Only executed if inner loop didn't break
    break  # Exit outer loop after finding target

print("Search concluded.")