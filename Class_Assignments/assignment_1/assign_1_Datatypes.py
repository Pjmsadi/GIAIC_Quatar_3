#1-Booleans


# Booleans can only have two values: True or False.
# Booleans are used to compare values and to evaluate expressions.
# Boolean values are the two constant objects False and True.
# They are used to represent truth values (other values can also be considered
# false or true).

# Boolean Example

a = True
b = False
c = 5 > 3

print(a, b, c)
# Output
# True False True
# In the above example, a and b are boolean variables. a is True, b is False, and c is True.
# Note: The first letter of True and False is capitalized.


#2-Complex

# Complex numbers are used to represent numbers like 1 + 2j.

# using complex

a = 1 + 2j
b = 3 - 4j
c = -5j

print(a,b,c)

# output

(1+2j) (3-4j) (-0-5j)



#3-Dictionary


# A dictionary stores data in key-value pairs.

# Creating a dictionary

a = {"name": "John", "age": 30, "city": "New York"}
b = {1: "apple", 2: "banana", 3: "cherry"}
c = {"name": "John", "age": 30, "city": "New York", "hobbies": ["reading", "coding", "traveling"]}
print(a, b, c,)

# Output

# {'name': 'John', 'age': 30, 'city': 'New York'} {1: 'apple', 2: 'banana', 3: 'cherry'} {'name': 'John', 'age': 30, 'city': 'New York', 'hobbies': ['reading', 'coding', 'traveling']}

# In the above example, a, b, and c are dictionary variables. a is {'name': 'John', 'age': 30, 'city': 'New York'}, b is {1: 'apple', 2: 'banana', 3: 'cherry'}, and c is {'name': 'John', 'age': 30, 'city': 'New York', 'hobbies': ['reading', 'coding', 'traveling']}.
# Accessing elements in a dictionary
# You can access elements in a dictionary by using their keys.

# Accessing elements in a dictionary

a = {"name": "John", "age": 30, "city": "New York"}
print(a["name"])
print(a["age"])
print(a["city"])

# Output

# John
# 30
# New York

# In the above example, we accessed the values of the keys "name", "age", and "city" in the dictionary a.



#4-Float


# Floats are decimal numbers, such as 3.14, -0.001, etc.

# Example of Floats

a = 3.14
b = -0.001
c = 0.0
print(a, b, c)
# Output
# 3.14 -0.001 0.0
# In the above example, a, b, and c are float variables. a is 3.14, b is -0.001, and c is 0.0.


#5-Integer


# Integers are whole numbers, such as 1, 2, -3, etc.


# Example of Integers
a = 1
b = 2
c = -3

print(a,b,c)

# output

1, 2,  -3

# In the above example, a, b, and c are integers.
# Note: Integers can be positive, negative, or zero.

# Integers can be used in arithmetic operations.

a = 10
b = 20
c = a + b

print(c)

# output

30

# In the above example, a and b are integers. c is the result of the addition of a and b.



#6-List


# A list is an ordered collection that can hold different data types.

# Creating a list

a = [1, 2, 3]
b = ["apple", "banana", "cherry"]
c = [1, "hello", 3.14]

print(a, b, c)

# Output

[1, 2, 3] ['apple', 'banana', 'cherry'] [1, 'hello', 3.14]
# In the above example, a, b, and c are list variables. a is [1, 2, 3], b is ['apple', 'banana', 'cherry'], and c is [1, 'hello', 3.14].
# Accessing elements in a list
# You can access elements in a list by using their index. The index starts from 0.



#7-NoneType



# None is a special data type that represents the absence of a value. It is often used to represent missing or undefined values. None is a singleton object in Python, which means that there is only one instance of None in memory.

# None Example

a = None
b = None
c = None

print(a, b, c)

# Output

# None None
# In the above example, a, b, and c are variables of type None. They all have the value None.

# Note: None is not the same as False or an empty string (""). None is a distinct data type in Python that represents the absence of a value.

# None is often used as a default value for function arguments or as a placeholder for variables that have not been assigned a value yet.

# None as a default value for function arguments

def greet(name=None):

    if name is None:
        print("Hello, anonymous!")
    else:
        print(f"Hello, {name}!")


greet()
greet("Alice")

# Output

# Hello, anonymous!
# Hello, Alice!

# In the above example, the greet function has a default argument name=None. If no argument is provided when calling the function, the default value None is used, and the function greets the user as "Hello, anonymous!". If an argument is provided, the function greets the user by name.

# None is also commonly used to initialize variables that may or may not have a value assigned to them later in the program.

# Initializing a variable with None

value = None

# Some code that may or may not assign a value to value

# if some_condition:
#     value = 42

# Using the value of the variable

if value is None:
    print("No value assigned yet!")
else:
    print(f"The value is {value}")

# Output

# No value assigned yet!

# In the above example, the variable value is initialized with None. Depending on some condition, a value may or may not be assigned to the variable later in the program. The value of the variable is checked using the is None comparison to determine if a value has been assigned.

# None is a useful data type in Python for representing the absence of a value and handling default or uninitialized variables. It is important to distinguish None from other values like False or an empty string, as they have different meanings and use cases.




#8-Set

# A set is an unordered collection that does not allow duplicate values.

# Creating a set

a = {1, 2, 3}
b = {"apple", "banana", "cherry"}
c = {1, "hello", 3.14}

print(a, b, c)

# Output

# {1, 2, 3} {'banana', 'apple', 'cherry'} {1, 'hello', 3.14}

# In the above example, a, b, and c are set variables. a is {1, 2, 3}, b is {'apple', 'banana', 'cherry'}, and c is {1, 'hello', 3.14}.
# Accessing elements in a set
# You cannot access elements in a set by using their index because sets are unordered. However, you can loop through the set to access its elements.
# Adding elements to a set
# You can add elements to a set using the add() method.

# Adding elements to a set

a = {1, 2, 3}
a.add(4)
print(a)

# Output

# {1, 2, 3, 4}
# In the above example, we added the element 4 to the set a using the add() method.
# Removing elements from a set
# You can remove elements from a set using the remove() method.

# Removing elements from a set

a = {1, 2, 3}
a.remove(2)
print(a)

# Output

# {1, 3}
# In the above example, we removed the element 2 from the set a using the remove() method.
# Set operations
# You can perform various set operations such as union, intersection, difference, and symmetric difference on sets in Python.



#9-String



# Strings represent text and are written in single or double quotes.

# String Example

a = "Hello"
b = 'World'
c = '''Hello, World!'''
print(a, b, c)
# Output
#  Hello World Hello, World!
# In the above example, a, b, and c are string variables. a is "Hello", b is 'World', and c is '''Hello, World!'''.





#10-Tuple


# A tuple is also an ordered collection, but its elements cannot be changed (immutable).

# Creating a tuple

a = (1, 2, 3)
b = ("apple", "banana", "cherry")
c = (1, "hello", 3.14)

print(a, b, c)

# Output

(1, 2, 3) ('apple', 'banana', 'cherry') (1, 'hello', 3.14)

# In the above example, a, b, and c are tuple variables. a is (1, 2, 3), b is ('apple', 'banana', 'cherry'), and c is (1, 'hello', 3.14).



