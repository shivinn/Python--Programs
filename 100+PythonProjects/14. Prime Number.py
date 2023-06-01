# Python program to print whether it is prime or not.

n = int(input(" Enter number: "))

if n == 1:
    print(" Not a Prime!")

if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print(" Not Prime!")
            break
    else:
        print(" Prime!")