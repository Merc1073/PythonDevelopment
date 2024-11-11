age = int(input("What is your age?: "))

if age < 0:
    print("You have not been born yet!")
elif age < 18:
    print("You are a minor.")
elif age >= 18 and not age > 64:
    print("You are an adult")
else:
    print("You are a senior")