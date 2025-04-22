# What is a Module in Python? — Super Easy Explanation



# A module is a file containing Python code. It can define functions, classes, and variables.
# A module can also include runnable code. The file name is the module name with the suffix .py added.

#  Example:
# modules.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b


#  What are the benefits of modules?

# Code Reuse – Write once, use anywhere.

# Readable – Keep code in separate files to make it clean and organized.

# Maintainable – If you find a bug, just fix it in that specific module.


# 🔹 Types of Modules:

# ✅ Built-in Modules : Come with Python,
# like math, random, os, datetime


import math
# Example usage of the math module

print(math.sqrt(16))  # Output: 4.0

#  Custom Modules : Modules you create yourself,
# like your own
#example: modules.py
import modules

# 🌐 Third-party Modules : You need to install these,

# like numpy, pandas, flask

import numpy as np


# How to Import a Module in Python?

# 1. Import the whole module
# You can access everything using module_name.something

import math
print(math.pi)       # Output: 3.141592653589793
print(math.sqrt(25)) # Output: 5.0


# 2. Import specific functions or classes
# Only bring in what you need.

from math import sqrt, pi
print(sqrt(36))  # Output: 6.0
print(pi)        # Output: 3.141592653589793

# 3. Import with an alias
# Use a shortcut name (alias) for convenience.

import numpy as np
arr = np.array([1, 2, 3])
print(arr)

# Output: [1 2 3]

# 4. Import all (not recommended)
# Brings everything from the module — not recommended due to potential conflicts.

from math import *
print(sin(0))  # Output: 0.0