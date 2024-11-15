# string = a sequence of characters used to represent text

# string example
stringExample = "Hello"


# outputs the length (int) of given string
print(len(stringExample))


# converts all characters in given string to be upper or lower case
print(stringExample.upper())
print(stringExample.lower())


# removes all whitespaces in given string
stringExample2 = "   Hello "
print(stringExample2.strip())


# removes all whitespace before string
print(stringExample2.lstrip())


# removes all whitespace after string
print(stringExample2.rstrip())


# replaces occurrences of a specified substring with another substring
print(stringExample.replace("Hel", "Goodbye"))


# find() returns the index of the first occurrence of a substring, or -1 if it’s not found
# index() is similar, but it raises an error if the substring is not found
text = "Hello, World!"
print(text.find("World"))  # Output: 7
print(text.index("World")) # Output: 7


# splits a string into a list of substrings based on a delimiter (default is whitespace)
text = "Hello, World!"
print(text.split())         # Output: ['Hello,', 'World!']
print(text.split(","))      # Output: ['Hello', ' World!']


# joins elements of an iterable (e.g., a list) into a single string, using the string as a separator
words = ["Hello", "World"]
print(" ".join(words))  # Output: "Hello World"


# checks if a string starts or ends with a specific substring
text = "Hello, World!"
print(text.startswith("Hello"))  # Output: True
print(text.endswith("!"))        # Output: True


# capitalize() capitalizes the first letter
# title() capitalizes the first letter of each word
# swapcase() swaps uppercase to lowercase and vice versa
text = "hello world"
print(text.capitalize())  # Output: "Hello world"
print(text.title())       # Output: "Hello World"
print(text.swapcase())    # Output: "HELLO WORLD"


# counts occurrences of a substring in the string
text = "Hello, World!"
print(text.count("o"))  # Output: 2


# isalpha() returns True if all characters are letters
# isdigit() returns True if all characters are digits
# isalnum() returns True if all characters are letters or digits
text = "Hello"
print(text.isalpha())  # Output: True
text = "123"
print(text.isdigit())  # Output: True
text = "Hello123"
print(text.isalnum())  # Output: True


# used for formatting strings with placeholders {}
name = "Alice"
age = 30
print("My name is {} and I am {} years old.".format(name, age))
# Output: "My name is Alice, and I am 30 years old."

print(f"My name is {name} and I am {age} years old.")
# Output: "My name is Alice, and I am 30 years old."


# aligns the string to the center, left, or right within a specified width
text = "Hello"
print(text.center(10))   # Output: "  Hello   "
print(text.ljust(10))    # Output: "Hello     "
print(text.rjust(10))    # Output: "     Hello"

text = "   Python programming is fun!   "
# convert to uppercase, strip whitespace, replace "fun" with "awesome", and split into words
result = text.strip().replace("fun", "awesome").upper().split()
print(result)  # Output: ['PYTHON', 'PROGRAMMING', 'IS', 'AWESOME']