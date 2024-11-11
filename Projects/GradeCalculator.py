"""
Objective:

Write a program that takes a score as input
and returns a grade based on the following scale:

90-100: A
80-89: B
70-79: C
60-69: D
Below 60: F

"""

# my attempt
score = int(input("Enter the score for your exam to determine your grade: "))

if score >= 90:
    print("You achieved an: A")
elif score >= 80:
    print("You achieved a: B")
elif score >= 70:
    print("You achieved a: C")
elif score >= 60:
    print("You achieved a: D")
else:
    print("You achieved a: F")



# correct solution
score = int(input("Enter your score: "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")