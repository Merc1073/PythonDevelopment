"""

Objective:

Write a function called create_contact_book() that:

1. Initializes an empty dictionary called contact_book.
2. Takes user input to add multiple contacts to the dictionary,
3. where the contact name is the key and the phone number is the value.

Allows the user to:
1. Add a new contact
2. Update an existing contact's number
3. Remove a contact
4. View all contacts

Print messages for each operation to guide the user
and show the updated contact_book after each change.

"""


def create_contact_book():
    contact_book = {}

    while True:
        try:
            user_input = int(input("What would you like to do?:\n\n"
                                   "1. Add a new contact\n"
                                   "2. Update an existing contact's number\n"
                                   "3. Remove a contact\n"
                                   "4. View all contacts\n"
                                   "5. Quit\n"))
        except ValueError:
            print("Have to enter a number.")

        else:
            match user_input:
                case 1:
                    user_key = input("Enter the name of your contact: ")
                    user_value = input("Enter the phone number of your contact: ")
                    contact_book[user_key] = user_value
                case 2:
                    if not contact_book:
                        print("No contacts available to change phone number of.\n")
                    else:
                        user_key = input("Enter the name of the contact whose phone number you wish to change: ")
                        user_value = input("What phone number would you like to change it to?: ")
                        contact_book[user_key] = user_value
                case 3:
                    if not contact_book:
                        print("There are no contacts to remove.\n")
                    else:
                        user_key = input("Enter the name of the contact you wish to remove: ")
                        del contact_book[user_key]
                case 4:
                    if not contact_book:
                        print("Your contact book is empty...\n")
                    else:
                        print("Here is your current contact book:\n")
                        for key, value in contact_book.items():
                            print(key, ":", value)
                case 5:
                    break
                case _:
                    print("Invalid input.")


print("Thank you for using our program!\n"
      "See you next time.")

create_contact_book()




# correct solution
def create_contact_book2():
    contact_book = {}

    while True:
        try:
            user_input = int(input("What would you like to do?:\n\n"
                                   "1. Add a new contact\n"
                                   "2. Update an existing contact's number\n"
                                   "3. Remove a contact\n"
                                   "4. View all contacts\n"
                                   "5. Quit\n"))
        except ValueError:
            print("Invalid input! Please enter a number from 1 to 5.\n")
            continue

        match user_input:
            case 1:
                user_key = input("Enter the name of your contact: ")
                user_value = input("Enter the phone number of your contact: ")
                contact_book[user_key] = user_value
                print(f"Contact '{user_key}' added successfully!\n")

            case 2:
                if not contact_book:
                    print("No contacts available to update.\n")
                else:
                    user_key = input("Enter the name of the contact to update: ")
                    if user_key in contact_book:
                        user_value = input("Enter the new phone number: ")
                        contact_book[user_key] = user_value
                        print(f"Contact '{user_key}' updated successfully!\n")
                    else:
                        print(f"Contact '{user_key}' not found in your contact book.\n")

            case 3:
                if not contact_book:
                    print("No contacts available to remove.\n")
                else:
                    user_key = input("Enter the name of the contact to remove: ")
                    if user_key in contact_book:
                        del contact_book[user_key]
                        print(f"Contact '{user_key}' removed successfully!\n")
                    else:
                        print(f"Contact '{user_key}' not found in your contact book.\n")

            case 4:
                if not contact_book:
                    print("Your contact book is empty.\n")
                else:
                    print("Here is your current contact book:")
                    for key, value in contact_book.items():
                        print(f"{key}: {value}")
                    print()  # Blank line for readability

            case 5:
                print("Thank you for using our program!\nSee you next time.")
                break

            case _:
                print("Invalid option! Please enter a number from 1 to 5.\n")

create_contact_book2()
