# functions = allows reusability of code

# creating a function
def greet():
    print("Hello, welcome!")

# calling a function
greet()


# inserting parameters into function
def greet(name):
    print(f"Hello, {name}!")

greet("Miranda")


# returning a value
def add(a, b):
    return a + b

# storing the returned value inside another variable
result = add(3, 5)
print(result)


# creating default values for parameters in case none are specified during declaration
def greet(name="User"):
    print(f"Hello, {name}!")

greet()
greet("Daniels")