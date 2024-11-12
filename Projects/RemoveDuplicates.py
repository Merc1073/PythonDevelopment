"""
Objective:

Create a list with some duplicate values.
Use the count() and remove() methods to remove any duplicates.

"""

# my solution ( I was not able to figure out how
# to use the methods above to remove duplicates :< )
duplicate_list = [1, 2, 5, 8, 5, 3, 6, 8, 6, 5, 2, 1, 6, 9, 6, 3, 4]
print(duplicate_list)

duplicate_list = set(duplicate_list)
duplicate_list = list(duplicate_list)

print(duplicate_list)




# correct solution
items = ["apple", "banana", "apple", "orange", "banana"]

for item in items:
    while items.count(item) > 1:
        items.remove(item)

print("List without duplicates:", items)