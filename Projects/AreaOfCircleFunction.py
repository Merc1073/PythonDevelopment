"""
Objective:

Write a function circle_area(radius) that returns the area of a circle with the given radius.
Use the formula: area = π * radius^2. (Use 3.14159 as the value of π.)

"""
# my attempt
from math import pi

def circle_area(radius):
    return pi * radius ** 2

result = circle_area(5)
print(result)



# correct solution
def circle_area(radius):
    m_pi = 3.14159
    return m_pi * (radius ** 2)

print("Area:", circle_area(5))  # Output: Area: 78.53975