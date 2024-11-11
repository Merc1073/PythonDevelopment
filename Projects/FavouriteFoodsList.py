"""
Objective:

Write a program that creates a list of your five favorite foods, prints each food,
and then adds a new favorite food at the end.

"""

# my attempt
favourite_foods = []

for i in range(5):
    answer = input(f"Enter favourite food # {i+1}: ")
    favourite_foods.append(answer)

print()
print("Here is your favourite foods list: ")

for j in range(len(favourite_foods)):
    print(favourite_foods[j], end=", ")

print()
print()

favourite_foods.append("Raisins")

print(f"Oh wait, here, let me add this new food to your favourites: {favourite_foods[-1]}\n>;)\n")
print("Here is your new favourite foods list: ")
print(favourite_foods)




# correct solution
favorite_foods = ["pizza", "sushi", "pasta", "ice cream", "burger"]

for food in favorite_foods:
    print(food)

favorite_foods.append("tacos")
print("Updated list:", favorite_foods)