"""
Objective:

Create a file called math_tools.py.
Add a function square(n) that returns the square of a number
and a function cube(n) that returns the cube.
Import and use these functions in your main program.

"""

# my attempt
from CustomModules import math_tools

result1 = math_tools.square(5)
result2 = math_tools.cube(5)

print(result1, result2)



# correct solution
# they created a separate python file called math_tools and put these functions inside
def square(n):
    return n * n

def cube(n):
    return n * n * n

#import math_tools

print("Square of 3:", math_tools.square(3))  # Output: 9
print("Cube of 3:", math_tools.cube(3))      # Output: 27
