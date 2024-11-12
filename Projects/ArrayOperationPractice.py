"""

Objective:

Write a function called array_operations that:

Takes an array of integers as input.
Prompts the user to:

1. Add a new number to the end of the array (O(1) average).
2. Remove a specified number from the array (O(n)).
3. Insert a number at a specified index (O(n)).
4. Display the modified array and its length (O(1)).

"""

# my attempt
from random import randint

def array_operations(array):
    while True:
        try:
            user_input = int(input("What would you like to do to your array?:\n\n"
                               "1. Add a new number\n"
                               "2 .Remove a specific number\n"
                               "3. Insert a number at index\n"
                               "4. Display your array\n"
                               "5. Quit\n"))

        except ValueError:
            print("Must enter a valid number (1 - 5).")
            continue

        if user_input == 1:
            user_value = int(input("What number would you like to add?: "))
            array.append(user_value)
            print(f"Number {user_value} has been added to the end of the list.\n")
        elif user_input == 2:
            user_value = int(input("What number would you like to remove?: "))
            if user_value in array:
                array.remove(user_value)
                print(f"Number {user_value} has been removed from the list.\n")
            else:
                print(f"Number {user_value} is not inside the list.\n")
        elif user_input == 3:
            user_index = int(input("What index would you like to insert your number to?: "))
            user_value = int(input("What value would you like to add to your index?: "))
            array.insert(user_index, user_value)
        elif user_input == 4:
            print(f"Here is your array (length of {len(array)}):\n")
            for number in array:
                print(number, end=", ")
            print("\n")
        elif user_input == 5:
            print("Exiting application...\n")
            break
        else:
            print("Please enter a valid option.\n")

num_list = []
# generate a list with random numbers
for i in range(11):
    num_list.append(randint(1, 10))

array_operations(num_list)




# correct solution
from random import randint


def array_operations2(array):
    while True:
        try:
            user_input = int(input("What would you like to do to your array?:\n\n"
                                   "1. Add a new number\n"
                                   "2. Remove a specific number\n"
                                   "3. Insert a number at index\n"
                                   "4. Display your array\n"
                                   "5. Quit\n"))
        except ValueError:
            print("Must enter a valid number (1 - 5).")
            continue

        if user_input == 1:
            user_value = int(input("What number would you like to add?: "))
            array.append(user_value)
            print(f"Number {user_value} has been added to the end of the list.\n")

        elif user_input == 2:
            user_value = int(input("What number would you like to remove?: "))
            if user_value in array:
                array.remove(user_value)
                print(f"Number {user_value} has been removed from the list.\n")
            else:
                print(f"Number {user_value} is not inside the list.\n")

        elif user_input == 3:
            user_index = int(input("What index would you like to insert your number at?: "))
            user_value = int(input("What value would you like to add at that index?: "))

            if 0 <= user_index <= len(array):
                array.insert(user_index, user_value)
                print(f"Number {user_value} has been inserted at index {user_index}.\n")
            else:
                print(f"Invalid index! Please choose an index between 0 and {len(array)}.\n")

        elif user_input == 4:
            print(f"Here is your array (length of {len(array)}):")
            print(", ".join(map(str, array)) + "\n")

        elif user_input == 5:
            print("Exiting application...\n")
            break

        else:
            print("Please enter a valid option.\n")


# Generate a list with random numbers
num_list = [randint(1, 10) for _ in range(11)]

array_operations2(num_list)
