# Python program to find the square root of a number

# Two Solutions
# Solution 1.1: Using Exponentiation - pre-defined
num = 64
num1 = num ** 0.5
print(f" Square Root of {num}: ", num1)

# Solution 1.2: Using Exponentiation - User defined
num = float(input(" Enter a Number: "))
num1 = num ** 0.5
print(f" Square Root of {num}: ", num1)

# Solution 2: Using math module
import math as m

num = float(input(" Enter a Number: "))
num1 = m.sqrt(num)
print(f" Square Root of {num}: ", num1)