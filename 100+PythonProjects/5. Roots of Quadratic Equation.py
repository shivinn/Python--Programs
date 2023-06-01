# Python Program to solve & find Quadratic Equation
# Solution : Roots of Quadratic Equation

# We will use cmath module cmath - complex math module
# We use cmath module instead of math module because math module's square root
# function cannot calculate sqrt of negative number.

# Quadratic Equation - ax**2 + bx + c = 0
# a, b, and c are real numbers
# a != 0

import cmath

a = int(input(" Enter a (!=0): "))
b = int(input(" Enter b: "))
c = int(input(" Enter c: "))

# formula for discriminant

d = (b**2) - (4*a*c)

root1 = (-b - cmath.sqrt(d))/(2*a)
root2 = (-b + cmath.sqrt(d))/(2*a)

print(f" Root 1: {root1}")
print(f" Root 2: {root2}")