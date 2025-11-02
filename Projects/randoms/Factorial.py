import math
import sys

sys.set_int_max_str_digits(10**6)

num = int(input("Enter a number to calculate its factorial: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = math.factorial(num)
    print(f"The factorial of {num} is: {result}")

lst = [1, 5, 7, 9, 14]

for i in range(len(lst)):
    pass

num = input(int("Enter number: "))

for i in range(len(num)):
    num *= num
    num - 1

print(num)