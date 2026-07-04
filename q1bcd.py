"""
DTS 216 - Question 1b, 1c, 1d
b. Demonstrate use of lists, tuples, dictionaries, and sets.
c. Show type conversion between int, float, and string.
d. Print prime numbers between 1 and 100 using loops and loop control statements.
"""

# ---------------------------------------------------------------
# (b) LISTS, TUPLES, DICTIONARIES, SETS
# ---------------------------------------------------------------
print("=== (b) Data Structures Demo ===")

# List: ordered, mutable collection
courses = ["Python", "Statistics", "Database", "Networking", "AI"]
courses.append("Machine Learning")
print("List (courses):", courses)

# Tuple: ordered, immutable collection
coordinates = (6.5244, 3.3792)  # example: Lagos latitude, longitude
print("Tuple (coordinates):", coordinates)

# Dictionary: key-value pairs
student = {"name": "Animashaun Ademola Solomon", "matric_no": "DSA/2024/1037", "level": "200"}
print("Dictionary (student):", student)

# Set: unordered collection of unique items
grades_set = {"A", "B", "C", "A", "B"}  # duplicates automatically removed
print("Set (grades_set):", grades_set)

# ---------------------------------------------------------------
# (c) TYPE CONVERSION
# ---------------------------------------------------------------
print("\n=== (c) Type Conversion Demo ===")

num_int = 25
num_float = float(num_int)          # int -> float
num_str = str(num_float)            # float -> string
back_to_int = int(num_float)        # float -> int

print(f"Original int: {num_int} ({type(num_int)})")
print(f"Converted to float: {num_float} ({type(num_float)})")
print(f"Converted to string: '{num_str}' ({type(num_str)})")
print(f"Converted back to int: {back_to_int} ({type(back_to_int)})")

# ---------------------------------------------------------------
# (d) PRIME NUMBERS BETWEEN 1 AND 100
# ---------------------------------------------------------------
print("\n=== (d) Prime Numbers Between 1 and 100 ===")

primes = []
for num in range(2, 101):
    is_prime = True
    for divisor in range(2, int(num ** 0.5) + 1):
        if num % divisor == 0:
            is_prime = False
            break  # loop control: stop checking once a divisor is found
        else:
            continue  # loop control: keep checking next divisor
    if is_prime:
        primes.append(num)

print(primes)
print(f"Total prime numbers between 1 and 100: {len(primes)}")
