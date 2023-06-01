# Python program to print prime number in a given interval of numbers.
# Solution

l = int(input(" Enter Lower Limit: "))
u = int(input(" Enter Upper Limit: "))

for num in range(l, u+1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)