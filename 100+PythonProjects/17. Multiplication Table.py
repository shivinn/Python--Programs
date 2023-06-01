# Python program to display the multiplication table

n = int(input(" Enter number to display its multiplication table: "))

print(f" Multiplication Table of {n}")
for i in range(1,11):
    print(f" {n} * {i} = {n*i}")
