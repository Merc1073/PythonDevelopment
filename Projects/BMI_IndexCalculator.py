# my attempt
def calculate_bmi():
    while True:
        while True:
            try:
                weight = float(input("Please enter your weight in Kilograms (KG): "))
                height = float(input("Please enter your height in meters (m): "))
                break
            except ValueError:
                print("You have to enter numerical value. Please try again")

        try:
            bmi = weight / (height ** 2)
            print(f"Your BMI is: {bmi}.")

            if bmi < 18.5:
                print("You are underweight.")
            elif bmi < 24.9:
                print("You have a normal weight.")
            elif bmi < 29.9:
                print("You are overweight.")
            elif bmi > 30:
                print("You are obese.")
            else:
                print("Invalid input.")
        except ZeroDivisionError:
            print("Cannot divide by zero.")

        answer = input("Would you like to input your weight and height again? (y/n): ").strip().lower()
        while True:
            if answer in {"yes", "y"}:
                print("Restarting...")
                break
            elif answer in {"no", "n"}:
                break
            else:
                answer = input("Please input either 'yes/y' or 'no/n'.")

        if answer in {"no", "n"}:
            print("See you later!")
            break



# optimised solution
def calculate_bmi2():
    while True:
        try:
            weight = float(input("Please enter your weight in kilograms (KG): "))
            height = float(input("Please enter your height in meters (m): "))

            if weight <= 0 or height <= 0:
                print("Weight and height must be positive numbers. Please try again.")
                continue

            bmi = weight / (height ** 2)
            print(f"\nYour BMI is: {bmi:.2f}")

            if bmi < 18.5:
                print("You are underweight.")
            elif bmi < 24.9:
                print("You have a normal weight.")
            elif bmi < 29.9:
                print("You are overweight.")
            else:
                print("You are obese.")
        except ValueError:
            print("Invalid input. Please enter numerical values only.")
            continue
        except ZeroDivisionError:
            print("Height cannot be zero. Please try again.")
            continue

        answer = input("\nWould you like to calculate your BMI again? (yes/y or no/n): ").strip().lower()
        if answer not in {"yes", "y"}:
            print("Goodbye!")
            break