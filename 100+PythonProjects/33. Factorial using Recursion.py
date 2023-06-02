# Python program to find the factorial of number using recursion
# Solution

def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)


n = int(input(" Enter n: "))

print(" Factorial of {} is {}.".format(n, fact(n)))
