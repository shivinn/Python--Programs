# Python Program to check whether entered number is armstrong or not.
# Solution
# armstrong number verification:

sum = 0
n = int(input(" Enter number : "))
order = len(str(n))
temp = n

while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10

if sum == n:
    print(" It is an Armstrong Number!")
else:
    print(" Not an Armstrong Number!")