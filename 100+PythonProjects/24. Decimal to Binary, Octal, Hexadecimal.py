# Python program to convert decimal to binary, octal & hexadecimal
# Solution: using inbuilt functions

decimal = int(input(" Enter number: "))

print(f" The conversion of {decimal} is: ")

print(f"Binary equivalent: {bin(decimal)}")
print(f"Octal equivalent: {oct(decimal)}")
print(f"Hexadecimal equivalent: {hex(decimal)}")