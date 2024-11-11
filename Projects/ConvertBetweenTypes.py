"""
Objective:

Write a program that takes a floating-point number and converts it
to an integer, a string, and a boolean, then prints each result.

"""

# my attempt
num1 = float(input("Enter your decimal number: "))

num1 = int(num1)
print(f"Integer: {num1}.")

num1 = str(num1)
print(f"String: {num1}.")

num1 = bool(num1)
print(f"Boolean: {num1}.")



# correct solution
my_float = float(input("Enter a decimal number: "))

print("Integer:", int(my_float))
print("String:", str(my_float))
print("Boolean:", bool(my_float))