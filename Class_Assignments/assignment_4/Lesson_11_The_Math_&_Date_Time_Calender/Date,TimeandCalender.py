# 🕓 Date & Time in Python
# ⏱️ What Are Tick Intervals?
# Tick intervals refer to the number of seconds between two time events.

# In Python, time intervals are represented as floating-point numbers — they count the seconds since a specific reference point.

# 📅 What Is the Epoch?
# Epoch = A fixed point in time used as a reference for calculating time.

# In Python, the epoch is: January 1, 1970, 00:00:00 UTC

# This moment is the starting point for time calculations — like zero on a number line.

# 📢 Pronunciation:
# British: ee·pok

# American: eh·puhk

#  Why Use an Epoch?
# ✅ Consistent Timekeeping
# All systems can measure time the same way, no matter when or where they're running.

# ✅ Simplified Calculations
# It's easier to compute differences and store time as a single number (seconds since the epoch) than to deal with full date-time formats.

#  Epoch in Python — time Module

import time

# Current time in seconds since epoch
now = time.time()
print(now)  # Example: 1713781424.563284

# Convert to UTC time structure
utc_time = time.gmtime(now)
print(utc_time)

# Convert to local time structure
local_time = time.localtime(now)
print(local_time)


#  Using the time module
import time

# Get current time in seconds since the epoch
current_time = time.time()
print("Seconds since epoch:", current_time)

# Using the datetime module (more human-friendly)
from datetime import datetime

# Get current date and time
now = datetime.now()
print("Current date and time:", now)

# also format it:
formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted date and time:", formatted_now)

# Want just the current time?
current_time = now.strftime("%H:%M:%S")
print("Current time:", current_time)   


# Getting the Formatted Time
# Getting formatted time in Python is super useful when you want to display the date and time in a human-readable way.

# Getting Formatted Time
from datetime import datetime

# Get current date and time
now = datetime.now()

# Format the datetime object
formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted Time:", formatted_time)

# Examples:
print(now.strftime("%A, %B %d, %Y"))     # Tuesday, April 22, 2025
print(now.strftime("%I:%M %p"))          # 03:45 PM
print(now.strftime("%Y/%m/%d - %H:%M"))  # 2025/04/22 - 15:45

# Getting the Calendar for a Month
# To get the calendar for a specific month in Python, you can use the built-in calendar module — it's simple and powerful.

# Example: Display Calendar for a Month

import calendar

# Set the year and month
year = 2025
month = 4

# Get the month's calendar as a multi-line string
month_calendar = calendar.month(year, month)
print(month_calendar)

# Example Output:
#    April 2025
# Mo Tu We Th Fr Sa Su
#     1  2  3  4  5  6
#  7  8  9 10 11 12 13
# 14 15 16 17 18 19 20
# 21 22 23 24 25 26 27
# 28 29 30 



# The Date Time

# Python Module: datetime
# The datetime module is used to work with dates and times — both together or separately.

#example:

from datetime import datetime

now = datetime.now()
print("Current date and time:", now)

#output:
# Current date and time: 2025-04-22 16:15:45.123456

#  Extracting Individual Components
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)


#  Formatting the Date and Time
# Use strftime() to format date/time into readable strings.

formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted date and time:", formatted_date)

# Output:
# Formatted: Tuesday, April 22, 2025 04:15 PM

#  Creating a Specific Date/Time
dt = datetime(2025, 12, 25, 10, 30)
print("Custom datetime:", dt)

#  Date Math: Adding/Subtracting Time

from datetime import timedelta

tomorrow = now + timedelta(days=1)
yesterday = now - timedelta(days=1)

print("Tomorrow:", tomorrow)
print("Yesterday:", yesterday)

# What is NaN in Python?
# NaN stands for "Not a Number" — it’s a special floating-point value used to represent missing, undefined,
#  or unrepresentable numerical data (like 0 divided by 0, or the square root of a negative number in real numbers).

# 🔹 Where Does NaN Come From?
# You’ll usually see NaN in:

# Math errors

# Invalid computations

# Data analysis (e.g., empty cells in a dataset)

# Creating NaN in Python
import math
import numpy as np

print(float('nan'))       # NaN
print(math.nan)           # NaN
print(np.nan)             # NaN (NumPy)

#  Important Notes
# NaN != NaN — Yes, NaN is not equal to itself!
x = float('nan')
print(x == x)  # False

# How to Check for NaN
import math
import numpy as np

# Using math
print(math.isnan(float('nan')))  # True

# Using numpy
print(np.isnan(np.nan))          # True

#  Where You'll Use NaN
# In data science (e.g., with Pandas or NumPy)

# In scientific computing

# When dealing with messy or incomplete data

# What is Infinity in Python?
# In Python, Infinity represents numbers that are beyond the largest possible floating-point value (positive or negative),
# or the result of operations that exceed normal number limits (e.g., dividing a number by zero).


# Positive and Negative Infinity
# You can create positive infinity and negative infinity using:
positive_infinity = float('inf')
negative_infinity = float('-inf')

print(positive_infinity)  # inf
print(negative_infinity)  # -inf

# Or using math or numpy:
import math
positive_infinity = math.inf
negative_infinity = -math.inf

import numpy as np
positive_infinity_np = np.inf
negative_infinity_np = -np.inf

# 🔹 Operations with Infinity
# Any number divided by zero results in Infinity (positive or negative).
print(1 / 0)    # Raises ZeroDivisionError
print(1.0 / 0)  # inf (positive infinity)
print(-1.0 / 0) # -inf (negative infinity)

# Infinity + a number = Infinity.

print(positive_infinity + 1000)  # inf
print(negative_infinity - 1000)  # -inf

# Infinity compared to other values:

# Positive infinity is greater than any number.

# Negative infinity is less than any number.

print(positive_infinity > 1000000)  # True
print(negative_infinity < -1000000) # True

# Infinity with NaN (Not a Number):

# NaN is neither greater nor less than Infinity or any other number.

# How to Check for Infinity

import math

print(math.isinf(positive_infinity))  # True
print(math.isinf(negative_infinity))  # True
print(math.isinf(1000))               # False

#  Practical Use of Infinity
# Initial values in algorithms (like setting a very high initial value for finding the minimum in search algorithms).

# Error handling or out-of-range values (e.g., 1/0).

# Numerical analysis (e.g., in scientific or statistical calculations).