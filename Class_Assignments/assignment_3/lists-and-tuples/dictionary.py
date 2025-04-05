# ================================================
# Dictionary Operations Demonstration
# ================================================

# ------------------
# Dictionary Creation
# ------------------
person: dict[str, str | int] = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print("\nInitial Dictionary:")
print(person)

# ------------------
# Element Access
# ------------------
print("\nAccess Operations:")
print(f"Name: {person['name']}")  # Direct key access
print(f"Age: {person.get('age')}")  # Using get() method

# Safe access with default value
print(f"Height: {person.get('height', 'Not available')}")

# ------------------
# Dictionary Modification
# ------------------
# Update existing value
person["age"] = 31
print("\nAfter Age Update:")
print(person)

# Add new key-value pair
person["country"] = "USA"
print("\nAfter Adding Country:")
print(person)

# ------------------
# Dictionary Methods
# ------------------
# keys() - Get dictionary keys
print("\nDictionary Keys:")
for key in person.keys():
    print(f"- {key}")

# values() - Get dictionary values
print("\nDictionary Values:")
for value in person.values():
    print(f"- {value}")

# items() - Get key-value pairs
print("\nDictionary Items:")
for key, value in person.items():
    print(f"{key}: {value}")

# update() - Merge dictionaries
person.update({"occupation": "Engineer", "age": 32})
print("\nAfter Update/Merge:")
print(person)

# pop() - Remove and return value
removed_value = person.pop("city")
print(f"\nRemoved 'city' value: {removed_value}")
print("After pop('city'):")
print(person)

# popitem() - Remove last inserted item
last_key, last_value = person.popitem()
print(f"\nRemoved last item: {last_key} = {last_value}")
print("After popitem():")
print(person)

# ------------------
# Dictionary Maintenance
# ------------------
# Clear dictionary
person.clear()
print("\nAfter clear():")
print(f"Dictionary contents: {person}")
print(f"Is empty? {not person}")

# Reinitialize dictionary
person = {
    "name": "Alice",
    "age": 28,
    "email": "alice@example.com"
}
print("\nReinitialized Dictionary:")
print(person)

# ------------------
# Advanced Operations
# ------------------
# Dictionary comprehension
squared_ages = {k: v**2 if isinstance(v, int) else v for k, v in person.items()}
print("\nDictionary Comprehension Example:")
print(squared_ages)

# Nested dictionaries
person["address"] = {
    "street": "123 Main St",
    "city": "Boston",
    "zipcode": "02101"
}
print("\nWith Nested Address:")
print(person)
print("Street:", person["address"]["street"])