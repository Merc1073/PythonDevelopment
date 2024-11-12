"""Objective:

Write a function called get_integer_input() that prompts the user to enter an integer.
The function should handle the following cases:

If the user enters a non-integer value (e.g., a letter),
catch a ValueError and print "Invalid input! Please enter an integer."

If the integer entered is negative,
raise a ValueError with the message "Only positive integers are allowed."

If the input is valid and positive,
print "Thank you for entering a positive integer!"

Include a finally block that prints "Input process completed." at the end, regardless of the input.

"""

# my attempt
"""def get_integer_input(value):
    if type(value) != int:
        raise ValueError("Invalid Input! Please enter an integer.")
    elif value < 0:
        raise ValueError("Only positive integers are allowed.")
    else:
        try:
            print("Thank you for entering a positive integer!")
        finally:
            print("Input process completed.")

user_input = int(input("Enter a number to check if it is valid: "))

get_integer_input(user_input)"""




# correct solution

def get_integer_input_again():
    try:
        value = int(input("Enter a number to check if it is valid: "))
        if value < 0:
            raise ValueError("Only positive integers are allowed.")
        print("Thank you for entering a positive integer!")
    except ValueError as e:
        print(e)
    finally:
        print("Input process completed.")

get_integer_input_again()