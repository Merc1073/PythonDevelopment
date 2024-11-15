import random


"""Basic Functions"""

# outputs a random value from 0.0 and 1.0
print(random.random())

# outputs a random integer from given range
print(random.randint(1, 10))

# outputs any floating point number from given range
print(random.uniform(1, 10))



"""Working with Sequences"""

# outputs a random element from an array
colours = ["red", "orange", "yellow", "green", "blue", "purple", "brown", "black", "white"]
print(random.choice(colours))

# outputs a list of elements based on given count, can have duplicates
print(random.choices(colours, k=3))

# outputs a list of elements based on given count, with no duplicates
print(random.sample(colours, k=3))

# modifies the original list by shuffling the order
random.shuffle(colours)
print(colours)



"""Generating Random Numbers with a Specific Distribution"""

# generates a random float from a Gaussian Distribution
print(random.gauss(0, 1))

# generates a random float from an exponential distribution
print(random.expovariate(1.5))



"""Setting a Seed"""

# initializes a random number generator with a specified seed for repeatable results.
random.seed(10)

# this will now always give the same result with the same seed
print(random.randint(1, 10))