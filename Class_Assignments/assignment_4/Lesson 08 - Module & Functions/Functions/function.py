# What is a Function?
# A function is a block of code that performs a specific task. 
# You define a function once, and then you can call (use) it multiple times whenever needed.

# Benefits of using functions:

# Avoids code repetition

# Increases reusability

# Keeps your code clean and easy to understand



#  Structure of a Function
def function_name(parameters):
    # function body
    return function_name

# Example:
def add_numbers(a, b):
    result = a + b
    return result

# Calling the Function:
sum = add_numbers(3, 5)
print(sum)  # Output: 8

# Types of Functions
# 1. Built-in Functions
# These are the functions that Python provides by default.

#  Examples: print(), len(), range(), type(), int(), etc.
print("Hello")
length = len("Sadia")
print(length)  # Output: 5

# 2. User-defined Functions
# These are the functions that you create yourself using the def keyword.
# They can take parameters and return values.
# Example:
def greet(name):
    return f"Hello, {name}!"


#  Parameter:
# A parameter is the variable listed inside the parentheses when defining a function.
#  Example:
def add(a, b):  # 'a' and 'b' are parameters
    return a + b

# Argument:
# An argument is the actual value passed to the function when you call it.
#  Example:


def add(a, b):  # 'a' and 'b' are parameters
    return a + b

# 🔹 Return Statement
# If you want a function to give back a value, you use the return keyword.

# 📌 Example:

def square(x):
    return x * x

# When you call the function:

result = square(4)
print(result)  # Output: 16
# ✅ The return keyword sends the result back to where the function was called.
# If you don't use return, the function will return None by default.

#  What if you don’t use return?
# If a function has no return statement, it returns None by default.

# 📌 Example:

def greet(name):
    print("Hello", name)

output = greet("Sadia")
print(output)  # Output: Hello Sadia, then None


# Default Parameters
# You can give default values to parameters.
def greet(name="Guest"):
    print("Hello", name)

greet("Sadia")   # Hello Sadia  
greet()          # Hello Guest
# In the second call, since no argument is passed, it uses the default value "Guest".


#  Keyword Arguments
# You can call a function using keyword arguments, which allows you to specify the parameter names.
def student(name, age):
    print(name, age)

student(age=20, name="Ali")  # Output: Ali 20
student(name="Sara", age=25)  # Output: Sara 25
# In this case, the order of arguments doesn't matter because we are using keyword arguments.     


# Arbitrary Arguments
# When you're not sure how many arguments will be passed:

# *args → Multiple positional arguments

def add_all(*numbers):
    total = sum(numbers)
    return total

print(add_all(1, 2, 3, 4))  # Output: 10
print(add_all(5, 6))        # Output: 11
print(add_all(7, 8, 9, 10, 11))  # Output: 45   

# In this case, *args collects all the extra positional arguments into a tuple.
# **kwargs → Multiple keyword arguments

def show_details(**info):
    for key, value in info.items():
        print(key, ":", value)

show_details(name="Sadia", age=25, city="Lahore")
# Output:
# name : Sadia
# age : 25
# city : Lahore
# In this case, **kwargs collects all the extra keyword arguments into a dictionary.

#  Nested Functions
# You can define a function inside another function.
def outer_function():
    def inner_function():
        return "Hello from the inner function!"

    return inner_function()


#  Lambda Functions
# Lambda functions are small anonymous functions defined using the lambda keyword.
# They can take any number of arguments but can only have one expression.
# They are often used for short, throwaway functions.
# Example:

square = lambda x: x * x
print(square(5))  # Output: 25

# Lambda functions are often used in higher-order functions like map(), filter(), and reduce().

# What is a Generator Function?
# A generator function is a special type of function that yields values one at a time, instead of returning them all at once.

# You use the yield keyword instead of return.
# Syntax:
# def my_generator_function():
#     yield value1
#     yield value2
#     ...

# Example:
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

for num in count_up_to(5):
    print(num)
# Output:

# 1
# 2
# 3
# 4
# 5
# In this example, the count_up_to function is a generator that yields numbers from 1 to n.
# Each time you call next() on the generator, it resumes execution until it hits the next yield statement.
# This allows you to iterate over potentially large sequences without storing them all in memory at once.
# Generators are memory efficient and can be used to create infinite sequences.


# ✅ Key Features of Generator Functions:
# State saving: It remembers where it left off after each yield

# Lazy evaluation: Generates values on demand, not all at once

# Efficient: Uses less memory, great for working with large data


# What is a Simple Generator Function?
# A simple generator function is a function that uses the yield keyword to return values one at a time, 
# pausing between each value instead of returning everything at once.

# Example:
def simple_generator():
    yield 1
    yield 2
    yield 3

# This function yields three values: 1, 2, and 3.

# Every time you call next() on it, it gives the next value and remembers where it left off.

#  Using the Generator:
# Create a generator object
gen = simple_generator()

# Check type
print(type(gen))  # Output: <class 'generator'>

# Iterate over the generator
for value in gen:
    print(value)

# Output:
# 1
# 2
# 3


# 🧠 Key Points:
# yield pauses the function and saves its state.

# On the next call, it resumes right after the last yield.

# Generators are memory efficient — they don’t store all values at once.


# What is an Infinite Sequence?
# An infinite sequence keeps producing values forever — it doesn’t stop unless you stop it manually.

# With normal functions, this would crash your program or use a ton of memory. But with generators, it’s memory-efficient and safe.

# ✅ Example: Infinite Counter Generator

def infinite_counter():
    num = 1
    while True:
        yield num
        num += 1

# This will keep yielding 1, 2, 3, 4, ... forever.

# You control how many values you want to take.

#  How to Use It Safely:
gen = infinite_counter()

for _ in range(10):  # Only take first 10 numbers
    print(next(gen))
# Output:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# This way, you can safely use an infinite generator without crashing your program.
# You can also use break to stop the loop when you want:

# 🧠 Why Use Generator for Infinite Sequences?
# Doesn’t load everything in memory.

# Keeps running without crashing.

# You decide when to stop.

# Perfect for live data, event streams, etc.
