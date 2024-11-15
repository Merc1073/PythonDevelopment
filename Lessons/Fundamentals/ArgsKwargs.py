# *args = Arbitrary Positional Arguments
# allows to pass a variable number of arguments to a function


def add_numbers(*args):
    result = sum(args)
    print(f"The sum is: {result}.")

add_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
add_numbers(5, 10 , 15)


# you do not have to use the word "args" specifically.
# you can use any words, so long as you prefix it with a "*".

def multiply_numbers(*numbers):
    result = numbers[0]
    for num in numbers:
        result *= num
    print(result)

# outputs 1x2x3x4x5 = 120
multiply_numbers(1, 2, 3, 4, 5)



# **kwargs = Arbitrary Keyword Arguments
# passes a variable number or keyword arguments to a function
# it collects them into a dictionary


def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}, {value}.")

print_info(name="Alice", age=25, city="New York")


# args and kwargs can be combined

def display(*args, **kwargs):
    print("Positional Arguments: ", args)
    print("Keyword Arguments: ", kwargs)

display(1, 2, 3, name="Alice", age="25")


"""

Key Points:

*args is for variable positional arguments (returns a tuple).
**kwargs is for variable keyword arguments (returns a dictionary).

"""