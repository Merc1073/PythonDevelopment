"""
Objective:

Write a program with two functions: one that converts Celsius to Fahrenheit and one that converts Fahrenheit to Celsius.

Function: celsius_to_fahrenheit(Celsius)
Function: fahrenheit_to_celsius(Fahrenheit)
Use these functions in a program that allows the user to enter a temperature and convert it.

"""
from urllib.parse import uses_relative


# my attempt
def celsius_to_fahrenheit(celsius):
    return celsius * 1.8 + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 0.5556


while True:
    user_input = input("Which temperature would you like to convert to?\n"
                       "Celsius or Fahrenheit?:\n\n"
                       "1. C\n"
                       "2. F\n"
                       "3. Q (to quit program)")

    user_input = user_input.upper().strip()

    print()

    match user_input:
        case "C":
            answer = float(input("Enter your Celsius value: "))
            result = celsius_to_fahrenheit(answer)

            print(f"{answer}°C to Fahrenheit is: {result}°F.\n")

        case "F":
            answer = float(input("Enter your Fahrenheit value: "))
            result = fahrenheit_to_celsius(answer)

            print(f"{answer}°F to Celsius is: {result}°C.\n")

        case "Q":
            break

        case _:
            print("Please enter a valid measurement (°C or °F)\n")

print("See you later!")




# correct solution
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

choice = input("Convert from (C)elsius or (F)ahrenheit? ").strip().upper()
temperature = float(input("Enter the temperature: "))

if choice == "C":
    print("Temperature in Fahrenheit:", celsius_to_fahrenheit(temperature))
elif choice == "F":
    print("Temperature in Celsius:", fahrenheit_to_celsius(temperature))
else:
    print("Invalid choice.")
