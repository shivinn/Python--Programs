# Python Program to find the factor of a number
# Solution

x = int(input(" Enter number: "))

print(f" Factors of {x}: ")
for i in range(1, x+1):
    if x % i == 0:
        print(i)
