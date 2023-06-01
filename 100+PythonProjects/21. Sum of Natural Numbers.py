# Python Program to find the sum of natural numbers.
# Solution

n = int(input(" Enter the digit till you want the sum: "))
if n < 0:
    print(" Please enter positive number: ")
else:
    sum = 0
    for i in range(n+1):
        sum += i

print(f" Sum of {n} natural numbers: {sum}")
