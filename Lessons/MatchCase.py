# match = allows you to test a value against different patterns.

import random

randomNum = random.randint(1, 5)
print(randomNum, end="\n\n")

# syntax: match [variable_to_compare_against]
match randomNum:
    case 1:
        print("You've won a Giant Stuffed Animal!")
    case 2:
        print("You've won a Gift Card Bundle!")
    case 3:
        print("You've won a Mini Drone!")
    case 4:
        print("You've won a Retro Game Console!")
    case 5:
        print("You've won a Carnival Snack Basket!")
    case _:
        print("Nothing happens.")


# usual if-else statement variation:
if randomNum == 1:
    print("You've won a Giant Stuffed Animal!")
elif randomNum == 2:
    print("You've won a Gift Card Bundle!")
elif randomNum == 3:
    print("You've won a Mini Drone!")
elif randomNum == 4:
    print("You've won a Retro Game Console!")
elif randomNum == 5:
    print("You've won a Carnival Snack Basket!")
else:
    print("Nothing happens.")