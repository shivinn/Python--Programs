# Python program to find the factorial of a number

# Solution: Using for loop (iterative)
# n = int(input(" Enter number : "))
# fact = 1
# if n == 0:
#     print(fact)
# else:
#     for i in range(1,n+1):
#         # print(i)
#         fact *= i
#     print(f" Factorial of {n} is {fact}")

# Solution: Using Recursion

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)

n = int(input(" Enter number:"))
print(" Factorial of {} is {}".format(n, factorial(n)))