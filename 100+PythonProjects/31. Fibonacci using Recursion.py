# Python program to display fibonacci sequence using recursion
# Solution: Recursion

def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2) # 4th term + 3rd term = 5th term


n = int(input(" Enter n: "))
if n <= 0:
    print(" Enter a positive number!")
else:
    for i in range(n):
        print(fibo(i))