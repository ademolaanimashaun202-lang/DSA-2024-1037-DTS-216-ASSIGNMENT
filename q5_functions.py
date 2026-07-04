"""
DTS 216 - Question 5
a. Explain the term "function".
b. Explain string slicing [start:stop:step] and apply it.
c. Demonstrate the use of import math (math.pi).
"""

import math

# ---------------------------------------------------------------
# (a) WHAT IS A FUNCTION?
# ---------------------------------------------------------------
# A function is a named, reusable block of code that performs a specific
# task. It can accept inputs (parameters), execute a set of statements,
# and optionally return an output (a value) using the 'return' keyword.
# Functions help avoid code repetition and make programs easier to read,
# test, and maintain.
print("=== (a) Definition ===")
print("A function is a reusable block of code designed to perform a "
      "specific task. It is defined once using 'def' and can be called "
      "multiple times with different arguments.")


def add(a, b):
    """Example function that returns the sum of two numbers."""
    return a + b


print("Example call add(4, 6) ->", add(4, 6))

# ---------------------------------------------------------------
# (b) STRING SLICING [start:stop:step]
# ---------------------------------------------------------------
# String slicing extracts a portion of a string using the syntax
# string[start:stop:step]:
#   start -> index to begin at (inclusive), defaults to 0
#   stop  -> index to end at (exclusive), defaults to end of string
#   step  -> how many characters to move forward each time, defaults to 1
#            (a negative step reverses direction)
print("\n=== (b) String Slicing Demo ===")

s = "Python Programming"

part1 = s[0:6]          # "Python"
part2 = s[7:18]         # "Programming"
every_second = s[::2]   # every second character
reversed_str = s[::-1]  # reverse the string

print(f"Original string: '{s}'")
print(f'"Python" slice        -> s[0:6]  = "{part1}"')
print(f'"Programming" slice   -> s[7:18] = "{part2}"')
print(f'Every second character -> s[::2] = "{every_second}"')
print(f'Reversed string       -> s[::-1] = "{reversed_str}"')

# ---------------------------------------------------------------
# (c) import math DEMO
# ---------------------------------------------------------------
print("\n=== (c) import math Demo ===")

radius = 7
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

print(f"math.pi = {math.pi}")
print(f"Area of a circle with radius {radius} = {area:.2f}")
print(f"Circumference of a circle with radius {radius} = {circumference:.2f}")
