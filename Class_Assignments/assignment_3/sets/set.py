# A set does not allow duplicate elements
# List and Tuple can contain duplicates, but a Set cannot.

# Creating a set using curly braces
my_set: set = {123, 452, 5, 6}

# Creating a set using the set() constructor
my_set2: set = set([123, 452, 5, 6])

print("my_set              =", my_set)      # Output: {123, 452, 5, 6}
print("my_set2             =", my_set2)     # Output: {123, 452, 5, 6}
print("type(my_set)        =", type(my_set))  # <class 'set'>
print("type(my_set2)       =", type(my_set2)) # <class 'set'>
print("my_set == my_set2   =", my_set == my_set2)  # True (sets are equal regardless of order)

# Sets can only store immutable (hashable) objects.
# The following will raise a TypeError:
# my_set = {[123, 452, 5, 6]}  # Uncommenting this will raise: TypeError: unhashable type: 'list'

# Sets can contain multiple data types
multi_type_set: set = {7, 9.0, False, True, "Hello! World", (1, 5, 9, 'hi')}
print("multi_type_set      =", multi_type_set)
# Output (unordered): {False, True, 7, 9.0, 'Hello! World', (1, 5, 9, 'hi')}

# Sets are unordered, so the order of elements can vary at runtime
set3: set = {'Java', 'Python', 'Javascript', 'Java'}
print("set3                =", set3)  # Output may vary; duplicates removed

# Sets are unchangeable (you cannot update elements directly via index)
new_set: set = {1, 2, 3, 4, 5}
print("new_set             =", new_set)

try:
    new_set[0] = 10  # This will raise a TypeError
except TypeError as e:
    print("Error:", e)

# Set with mixed elements
my_new_set: set = {1, 2, 3, 4, 5, 'A', 'a'}
print("my_new_set          =", my_new_set)

# Removing specific elements
my_new_set.remove(3)
my_new_set.remove('A')
print("After removals      =", my_new_set)

# Adding a new element
my_new_set.add(6)
print("After adding 6      =", my_new_set)

# Removing multiple elements using difference_update()
my_new_set.difference_update({1, 5, 3, 'A'})  # Only elements that exist will be removed
print("After diff update   =", my_new_set)

# Adding multiple elements using update()
my_new_set.update([7, 8, 9, "Hello"])
print("After update        =", my_new_set)

# ----------------------------------------------------------------

# Set union using union() method
uni_set: set = {1, 2, 3, 5}
uni_set_2: set = {1, 5, 6, 7}
uni_set_3 = uni_set.union(uni_set_2)
print("Union (method)      =", uni_set_3)

# Set union using | operator
uni_set_4 = uni_set | uni_set_2
print("Union (| operator)  =", uni_set_4)
