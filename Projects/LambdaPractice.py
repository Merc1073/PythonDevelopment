"""

Objective:

Given a list of tuples (people [name:age]), write code to:

1. Sort people by age in ascending order
2. Sort people by the length of the name in ascending order

You should use the sorted() function with a lambda function as the key to achieve each sort.

"""

people = [("Alice", 30), ("Bob", 25), ("Charlie", 35), ("David", 20)]

# syntax: lambda arguments:expression

sorted_by_age = sorted(people, key=lambda person:person[1])
sorted_by_length = sorted(people, key=lambda person:len(person[0]))

print(sorted_by_age)
print(sorted_by_length)