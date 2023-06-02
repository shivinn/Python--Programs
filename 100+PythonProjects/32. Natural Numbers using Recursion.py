# Python Program to Find Sum of Natural Numbers using Recursion
# Solution

def nat(n):
    if n <= 1:
        return n
    else:
        return n + nat(n-1)


n = int(input(" Enter a number: "))

if n <= 0:
    print(" Enter a positive number!")
else:
    print(f" The sum of first {n} natural numbers is {nat(n)} ")

