# Python program to print fibonacci series
# Fibonacci Series: 0, 1, 1, 2, 3, 5, 8,...

n = int(input(" Enter number: "))

a = 0
b = 1
print(f"{a}\n{b}")
for i in range(2, n):
    c = a + b
    a = b
    b = c
    print(c)