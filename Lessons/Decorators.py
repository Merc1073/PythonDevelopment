# decorator = A function, which takes another function as an argument,
#             and returns a new function that extends the behaviour of the original.


# original function
def say_hello1():
    print("Hello!")

say_hello1()
print("\n")


# decorator that will extend the behaviour of the say_hello() function
def make_friendly(func):
    def wrapper():
        func()
        print("How are you doing?")
    return wrapper


@make_friendly
def say_hello2():
    print("Hello!")

say_hello2()



# example of a decorator that adds logging to a function

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args} and {kwargs}.")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}.")
        return result
    return wrapper


@log_decorator
def add(a, b):
    return a+b

@log_decorator
def subtract(a, b):
    return a-b

@log_decorator
def multiply(a, b):
    return a*b


add(3, 5)
subtract(3, 5)
multiply(3, 5)