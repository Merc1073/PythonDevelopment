"""
Objective:

Create a game where the computer randomly selects a
number between 1 and 100,and the user has to guess it.
The game should give feedback on whether the guess is
too high, too low, or correct.

1. Import the random module.
2. Generate a random number between 1 and 100.
3. Use a while loop to keep asking the user for their guess.
4. Provide feedback and break the loop when the guess is correct.

"""

import random


# my attempt
cpu_guess = random.randint(1, 100)

player_guess = 0
player_guess_counter = 0

while player_guess != cpu_guess:
    player_guess = int(input("Input a number from 1 to 100: "))
    if player_guess < 1 or player_guess > 100:
        print("Your number needs to be between 1 and 100.")
    elif player_guess > cpu_guess:
        player_guess_counter += 1
        print("Lower...")
    else:
        player_guess_counter += 1
        print("Higher...")

print(f"Congratulation, you've guessed the number correct!\nIt is: {cpu_guess}")
print(f"Total guesses: {player_guess_counter}.")



# correct solution
target = random.randint(1, 100)
guess = None

while guess != target:
    guess = int(input("Guess the number (between 1 and 100): "))

    if guess < target:
        print("Too low!")
    elif guess > target:
        print("Too high!")
    else:
        print("Congratulations! You guessed the number.")