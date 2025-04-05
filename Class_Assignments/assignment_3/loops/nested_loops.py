# ================================================
# Multiplication Table (Basic Nested Loop Version)
# ================================================

# Print tables from 1 to 9
for multiplier in range(1, 10):
    print(f"\nMultiplication Table of {multiplier}:")
    print("-" * 20)
    
    # Print table entries
    for multiplicand in range(1, 10):
        result = multiplier * multiplicand
        print(f"{multiplier} × {multiplicand:2} = {result:2}")
    
    print("-" * 20)