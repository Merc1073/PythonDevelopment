"""
Objective:

Write a program that asks the user for a number
and tells them if it’s even or odd.

"""

# my attempt
num = int(input("Enter your number to check if it is odd or even: "))

result = num % 2

if result == 0:
    print("Your number is even.")
else:
    print("Your number is odd")



# correct solution
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")