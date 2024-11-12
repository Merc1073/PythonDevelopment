"""
Objective:

Write a program that calculates the sum of all numbers in a list.

"""

# my attempt
numList = [1, 2, 3, 4, 5]
total = 0

for number in numList:
    total += number

print(total)



# correct solution
numbers = [5, 10, 15, 20]
total = sum(numbers)
print("The sum is:", total)