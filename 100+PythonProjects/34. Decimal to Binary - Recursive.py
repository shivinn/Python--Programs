# Python program to convert decimal to binary using recursion
# Solution:

def binary(n):
    if n > 1:
        binary(n//2)
    print(n % 2, end="")


n = int(input(" Enter n: "))
print("The binary of {}: ".format(n), end="")
binary(n)

