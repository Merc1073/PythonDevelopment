"""
Objective:

Write a program that asks the user for two numbers as strings,
converts them to integers, adds them together, and prints the result.

"""

# my attempt
string1 = str(input("Enter your first number: "))
string2 = str(input("Enter your second number: "))

string_to_num1 = int(string1)
string_to_num2 = int(string2)

result = string_to_num1 + string_to_num2

print(f"{string_to_num1} + {string_to_num2} = {result}.")



# correct solution
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

num1 = int(num1)
num2 = int(num2)

result = num1 + num2
print("The sum is:", result)