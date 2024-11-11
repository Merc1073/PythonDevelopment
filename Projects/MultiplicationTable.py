"""
Objective:

Write a program that prints the multiplication table for a given number up to 10.

"""

# my attempt
answer = int(input("Enter a number for a multiplication table: "))
print(f"Multiplication table for number {answer}:\n")

for i in range(11):
    print(f"{answer} * {i} = {answer * i}")


# correct solution
number = int(input("Enter a number: "))

for i in range(1, 11):
    print(number, "x", i, "=", number * i)
