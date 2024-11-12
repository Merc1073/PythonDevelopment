# modules = are Python files containing definitions and functions you can use.

# syntax: import [name_of_module]
import math

print(f"Square root of 16: {math.sqrt(16)}.")
print(f"Pi: {math.pi}.")


# can import specific functions instead of whole module
from random import randint

randomNumber = randint(1, 6)



# can import your custom made modules
import Functions

Functions.greet()