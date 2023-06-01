# Python Program to find HCF or GCD
# Solution

def calc_hcf(x, y):
    # i = 1
    # hcf = i
    if x > y:
        smaller = y
    else:
        smaller = x

    for i in range(1, smaller+1):
        if (x % i == 0) and (y % i == 0):
            hcf = i
    return hcf


x = int(input(" Enter x: "))
y = int(input(" Enter y: "))

print(f" The HCF or GCD of {x} and {y} is: {calc_hcf(x, y)}")