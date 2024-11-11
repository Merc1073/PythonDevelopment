"""
Objective:

Write a program that calculates the sum of
all numbers from 1 to 100 using a for loop.

"""

# my attempt
sumCount = 0

for i in range(100):
    sumCount += i
    print(sumCount)


# --------- correct answer ---------
total = 0
for i in range(1, 101):
    total += i
print("The sum is:", total)