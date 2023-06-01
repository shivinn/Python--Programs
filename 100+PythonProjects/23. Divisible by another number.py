# Python program to find the numbers divisible by another number

# Solution: for loop and conditional statements

# print(f" The numbers divisible by 13: ")
# for i in range(1, 100):
#     if i % 13 == 0:
#         print(i)

# Solution: Using Lambda function and filter()

l = [39, 48, 26, 98, 33, 67, 87]


result = list(filter(lambda x : x % 13 == 0, l))

print(f" The numbers divisible by 13 are: {result}")