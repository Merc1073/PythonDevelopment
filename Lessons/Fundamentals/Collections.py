"""

Lists: Can be ordered and changed, can store duplicates.
Sets: Cannot be ordered, but can be changed, cannot store duplicates.
Tuples: Can be ordered, but cannot be changed, can store duplicates.

"""

# List
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print all elements in array
print(numbers)

# print specific element in array (0 = first element)
print(numbers[0])

# print first three elements
print(numbers[0:3])

# print every second element
print(numbers[::2])

# print every element backwards
print(numbers[::-1])

# returns the length of array
print(len(numbers))

# returns True or False if element is found in array
print(5 in numbers)

# change specific element (possible because this is a list)
numbers[4] = 1073
print(numbers)

# adds element at the end of the list
numbers.append(7584)
print(numbers)

# remove a specific element from the list
numbers.remove(8)
print(numbers)

# inserts value at a given index
numbers.insert(2, 2759)
print(numbers)

# sorts your array alphabetically or in ascending order
numbers.sort()
print(numbers)

# sorts your array in reverse order
numbers.reverse()
print(numbers)

# returns index at position of given element in array
print(numbers.index(1073))

# returns count for amount of times given element appears in array
print(numbers.count(1073))

# clears your array, removes all elements
numbers.clear()
print(numbers)