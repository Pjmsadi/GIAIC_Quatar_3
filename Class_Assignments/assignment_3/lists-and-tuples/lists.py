# ================================================
# List Operations Demonstration
# ================================================

# ------------------
# List Creation
# ------------------
# Homogeneous lists
fruits: list[str] = ["apple", "banana", "cherry"]
numbers: list[int] = [10, 20, 30, 40]

# Heterogeneous list
mixed_data: list[object] = ["hello", 42, 3.14, True]

print("\nInitial Lists:")
print(f"Fruits: {fruits}")
print(f"Numbers: {numbers}")
print(f"Mixed Data: {mixed_data}")

# ------------------
# List Access & Modification
# ------------------
print("\nAccess Operations:")
print(f"First fruit: {fruits[0]}")       # Output: apple
print(f"Second from end: {fruits[-2]}")  # Output: banana

# Modify element using negative indexing
fruits[-3] = "watermelon"  # Replace first element
print(f"\nModified fruits list: {fruits}")

# ------------------
# List Slicing
# ------------------
print("\nSlicing Examples:")
print("First two fruits:", fruits[:2])       # ['watermelon', 'banana']
print("Every second item:", numbers[::2])    # [10, 30]
print("Reversed list:", mixed_data[::-1])    # [True, 3.14, 42, 'hello']

# ------------------
# List Methods
# ------------------
# Adding elements
fruits.append("mango")  # Add single element to end
print(f"\nAfter append: {fruits}")

fruits.extend(["grape", "kiwi"])  # Add multiple elements
print(f"After extend: {fruits}")

# Removing elements
removed_item = fruits.pop(2)  # Remove item at index 2 ('cherry')
print(f"\nRemoved item: {removed_item}")
print(f"After pop: {fruits}")

# ------------------
# List Sorting
# ------------------
numbers = [3, 1, 4, 1, 5, 9]

# Ascending sort (in-place)
numbers.sort()
print(f"\nSorted ascending: {numbers}")  # [1, 1, 3, 4, 5, 9]

# Descending sort (in-place)
numbers.sort(reverse=True)
print(f"Sorted descending: {numbers}")  # [9, 5, 4, 3, 1, 1]

# Create new sorted list (non-destructive)
unsorted = [5, 2, 8, 1]
sorted_list = sorted(unsorted)
print(f"\nOriginal: {unsorted}\nSorted: {sorted_list}")