# Python Program to make a Simple Calculator
# Solution:

print(" Simple Calculator")
con = "y"
print(" Operations : \n 1. Division \n 2. Multiplication \n 3. Subtraction \n 4. Addition")
while con != "n":
    num1 = float(input(" Enter number 1 : "))
    num2 = float(input(" Enter number 2 : "))
    choice = int(input(" Enter choice (number): "))
    if choice == 1:
        print(f" The division for {num1} and {num2} is {num1 / num2}")
    elif choice == 2:
        print(f" The multiplication for {num1} and {num2} is {num1 * num2}")
    elif choice == 3:
        print(f" The subtraction between {num1} and {num2} is {num1 - num2}")
    elif choice == 4:
        print(f" The addition operation for {num1} and {num2} is {num1 + num2}")
    else:
        print(" Wrong choice!!")

    con = input(" Do you want to continue (y/n)?")
