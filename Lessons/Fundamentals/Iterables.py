# iterable = any object able to return its elements one at a time,
#            meaning it can be "iterated" over.


# examples of iterables

example_list = [1, 2, 3, 4]
example_tuple = (5, 6, 7)
example_string = "Hello"
example_dictionary = {"A":1, "B":2, "C":3}
example_set = {8, 9, 10}


# using for loops to iterate through each element
for item in example_list:
    print(item, end=", ")
for item in example_tuple:
    print(item, end=", ")
for item in example_string:
    print(item, end=", ")
for item in example_dictionary:
    print(item, end=", ")
for item in example_set:
    print(item, end=", ")


# converting to an iterator
iter_list = iter(example_list)

print(next(iter_list)) # output: 1
print(next(iter_list)) # output: 2
print(next(iter_list)) # output: 3



# check if object is iterable
from collections.abc import Iterable

print(isinstance([1, 2, 3], Iterable))