"""
Objective:

Write a function calculate() that takes two numbers and an operator (+, -, *, /)
and returns the result.

"""

# my attempt
def calculate(num1, num2, operator):
    match operator:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '/':
            return num1 / num2
        case _:
            print("Invalid operator/numbers")

result = calculate(5, 8, "*")

print(result)




# correct solution
def calculate(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a / b
    else:
        return "Invalid operator"

print(calculate(5, 3, "+"))  # Output: 8
