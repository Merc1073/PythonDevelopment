num1 = 10          #Integer = whole numbers
num2 = 36.12345    #Float   = floating point numbers (Decimals)
word = "Hello"     #String  = holds a string of characters
is_running = True  #Boolean = either True or False

# printing individual variables
print(num1)
print(num2)
print(word)
print(is_running)

# string concatenation (combining strings with variables)
print(word + ", How are you doing?")

# F strings
print(f"{num1}, {num2}, {word}, {is_running}.")

# Type checking a variable (returns data type of variable)
print(type(num1), type(num2), type(word), type(is_running))