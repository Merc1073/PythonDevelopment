"""
Write a program that takes a score as input and returns a grade based on the following scale:

90-100: A
80-89: B
70-79: C
60-69: D
Below 60: F

"""

score = int(input("Enter the score for your exam to determine your grade: "))

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