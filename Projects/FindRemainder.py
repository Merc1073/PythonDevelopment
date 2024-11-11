"""
Objective:

Write a program that calculates the remainder
when one number is divided by another.

"""

# my attempt
num1 = int(input("Enter your dividend: "))
num2 = int(input("Enter your divisor: "))

remainder = num1 % num2

print(f"The remainder of {num1} / {num2} = {remainder}")



# correct solution
dividend = int(input("Enter the dividend: "))
divisor = int(input("Enter the divisor: "))
remainder = dividend % divisor
print("The remainder is:", remainder)