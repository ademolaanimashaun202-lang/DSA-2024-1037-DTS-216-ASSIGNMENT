"""
DTS 216 - Question 3: NumPy Practice
a. Create a (5,5) NumPy array of random integers between 1 and 100.
b. Perform indexing/slicing, boolean indexing (>50), and transpose.
c. Use universal functions: sqrt, mean, std.
"""

import numpy as np

# (a) Create a 5x5 array of random integers between 1 and 100
np.random.seed(42)  # for reproducible output
arr = np.random.randint(1, 101, size=(5, 5))
print("=== (a) Original 5x5 Array ===")
print(arr)

# (b) Indexing and slicing
print("\n=== (b) Indexing and Slicing ===")
print("Element at row 0, column 0:", arr[0, 0])
print("First row:", arr[0, :])
print("Last column:", arr[:, -1])
print("Sub-array (first 2 rows, first 3 columns):\n", arr[:2, :3])

# Boolean indexing: filter values greater than 50
print("\nValues greater than 50:", arr[arr > 50])

# Transpose the array
print("\nTransposed array:")
print(arr.T)

# (c) Universal functions
print("\n=== (c) Universal Functions ===")
print("Square root of array:\n", np.sqrt(arr))
print(f"\nMean of array: {np.mean(arr):.2f}")
print(f"Standard deviation of array: {np.std(arr):.2f}")
