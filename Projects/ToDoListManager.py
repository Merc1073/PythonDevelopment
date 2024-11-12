"""
Objective:

Create a simple to-do list manager that allows the user to
add tasks, remove tasks, and view the list.
Use a loop to repeatedly ask the user for an action until they decide to quit.

Prompt Options:

1. Add a new task.
2. Remove a task.
3. View all tasks.
4. Quit.

"""

# my attempt
tasks = []
task_input = None
task_count = 0

while True:
    user_input = int(input("What would you like to do?:\n"
                       "1. Add a task\n"
                       "2. Remove a task\n"
                       "3. View all tasks\n"
                       "4. Quit\n"))

    match user_input:
        case 1:
            task_input = input("What task would you like to add?: ")
            task_input = task_input.capitalize()
            tasks.append(task_input)
            print("\n")
        case 2:
            task_input = input("Which task would you like to remove?: ")
            if task_input in tasks:
                task_input = task_input.capitalize()
                tasks.remove(task_input)
                print("\n")
            else:
                print("That task is not inside your list.\n\n")
        case 3:
            print("Here are your tasks:\n")
            task_count = 0
            for task in tasks:
                task_count += 1
                print(f"{task_count}) {task}")
            print("\n")
        case 4:
            print("Quitting the program...\n")
            break
        case _:
            print("Please enter a valid input.\n\n")

print("Thank you for using our program!\n"
      "See you next time!\n\n")



# correct solution
to_do_list = []

while True:
    print("\nTo-Do List Manager")
    print("1. Add a new task")
    print("2. Remove a task")
    print("3. View all tasks")
    print("4. Quit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        task = input("Enter the task: ")
        to_do_list.append(task)
        print(f"'{task}' has been added.")
    elif choice == "2":
        task = input("Enter the task to remove: ")
        if task in to_do_list:
            to_do_list.remove(task)
            print(f"'{task}' has been removed.")
        else:
            print(f"'{task}' not found in the list.")
    elif choice == "3":
        print("\nYour To-Do List:")
        for task in to_do_list:
            print("-", task)
    elif choice == "4":
        print("Exiting To-Do List Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a valid option.")
