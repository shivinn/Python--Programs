# Python program to find the largest among 3 numbers

x,y,z = input(" Enter 3 numbers: ").split()
x,y,z = int(x), int(y), int(z)

if x > y and x > z:
    print(f" x:{x} is the largest among all.")
elif y > z and y > x:
    print(f" y:{y} is the largest among all.")
else:
    print(f" z:{z} is the largest among all.")