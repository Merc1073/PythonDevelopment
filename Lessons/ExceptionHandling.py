# exceptions: errors which occur during the execution of a program

"""

try:
    # Code that may raise an exception
except ExceptionType:
    # Code that runs if the specified exception occurs

"""

# Try running the code below to see if it executes an error
try:
    result = 10 / 0

# if the code above executes an error, specify error type here, and execute code
except ZeroDivisionError:
    print("You can't divide by zero!")


# else: Runs only if no exceptions are raised in the try block.
# finally: Always runs after the try block, whether or not an exception was raised.
# This is useful for cleanup actions, like closing files.
try:
    result = 10 / 2
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print("Division successful! Result:", result)
finally:
    print("This will run no matter what.")


# You can also raise exceptions using the raise keyword.
# This is helpful if you want to enforce certain conditions.
def check_positive(number):
    if number < 0:
        raise ValueError("The number must be positive.")
    else:
        print("The number is positive.")

check_positive(5)


def divide_numbers(a, b):
    try:
        result2 = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except TypeError:
        print("Error: Both inputs must be numbers!")
    else:
        print("The result is:", result)
    finally:
        print("Execution completed.")

divide_numbers(10, 0)  # Example call with zero division
divide_numbers(10, 'a')  # Example call with wrong type
divide_numbers(10, 2)  # Successful division