"""
DTS 216 - Question 4
a. Purpose of type() function, demonstrated on several values.
b. Operator precedence explained and evaluated.
c. break vs continue statements demonstrated.
"""

# ---------------------------------------------------------------
# (a) type() FUNCTION
# ---------------------------------------------------------------
# type() returns the data type (class) of the object passed to it.
# It is useful for checking what kind of value a variable holds,
# which helps with debugging and controlling program logic.
print("=== (a) type() Function Demo ===")
print("type(10)      ->", type(10))
print("type(10.5)    ->", type(10.5))
print("type(True)    ->", type(True))
print('type("hello") ->', type("hello"))

# ---------------------------------------------------------------
# (b) OPERATOR PRECEDENCE
# ---------------------------------------------------------------
# Python evaluates expressions following an order of precedence:
# 1. Parentheses ()
# 2. Exponentiation **
# 3. Multiplication *, Division /, Floor Division //, Modulus %
# 4. Addition +, Subtraction -
#
# For: 3 + 4 * 2 ** 2 - 1
# Step 1: 2 ** 2 = 4   (exponentiation first)
# Step 2: 4 * 4 = 16   (multiplication next)
# Step 3: 3 + 16 - 1   (addition/subtraction, left to right)
# Step 4: 19 - 1 = 18
print("\n=== (b) Operator Precedence Demo ===")
expression_result = 3 + 4 * 2 ** 2 - 1
print("3 + 4 * 2 ** 2 - 1 =", expression_result)

# ---------------------------------------------------------------
# (c) break vs continue
# ---------------------------------------------------------------
# break: immediately terminates the loop entirely.
# continue: skips the rest of the current iteration and moves to the next one.
print("\n=== (c) break vs continue Demo ===")

print("(ii) Loop that prints 1 to 10 but skips 5 using continue:")
for i in range(1, 11):
    if i == 5:
        continue  # skip printing 5, move to next iteration
    print(i, end=" ")
print()

print("\n(iii) Loop that stops at 5 using break:")
for i in range(1, 11):
    if i == 5:
        break  # stop the loop entirely once 5 is reached
    print(i, end=" ")
print()
