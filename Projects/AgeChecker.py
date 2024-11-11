"""
Objective:

Create a program that asks for a person’s age
and tells them if they are a minor, an adult, or a senior (65+).

"""

# my attempt
age = int(input("What is your age?: "))

if age < 0:
    print("You have not been born yet!")
elif age < 18:
    print("You are a minor.")
elif age >= 18 and not age > 64:
    print("You are an adult")
else:
    print("You are a senior")



# correct solution
age = int(input("Enter your age: "))

if age < 18:
    print("You are a minor.")
elif age >= 65:
    print("You are a senior.")
else:
    print("You are an adult.")