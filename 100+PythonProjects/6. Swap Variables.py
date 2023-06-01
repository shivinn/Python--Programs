# Python Program to swap values stored in variables.

# Solutions
# Solution 1.1: Using third variable
x = 13
y = 12

print(f" Value of x & y before swapping\n x: {x}, y: {y}")

temp = x
x = y
y = temp

print(f" Value of x & y before swapping\n x: {x}, y: {y}")

# Solution 1.2: Without using third variable

print(f"\n Value of x & y before swapping\n x: {x}, y: {y}")

x, y = y, x

print(f" Value of x & y before swapping\n x: {x}, y: {y}")