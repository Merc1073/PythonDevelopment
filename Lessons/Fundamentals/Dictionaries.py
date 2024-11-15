# dictionary = a collection of key:value pairs.

# dictionary of students and their GPA scores
students = {
    "Jonathan":3.5,
    "Stacy": 2.7,
    "Robert": 3.1
}


# outputs the value for the key "Jonathan" in our dictionary of students
# if the key is not found, will return an error
print(students["Jonathan"])

# get() checks if it exists, then returns it, avoiding a KeyError exception
print(students.get("Stacy"))

# adding a new key and value
students["Percy"] = 2.0
print(students)

# deleting a key value pair
del students["Jonathan"]
print(students)

# remove a key value pair using pop()
previous_student = students.pop("Stacy")
print(previous_student)
print(students)

# outputting all keys
for key in students:
    print(key)

# outputting all values
for value in students.values():
    print(value)

# outputting both keys and values
for key, value in students.items():
    print(key, ":", value)

# prints all keys in dictionary
print(students.keys())

# prints all values in dictionary
print(students.values())

# prints all keys and values in dictionary
print(students.items())

# clears all keys and values in dictionary
students.clear()