def bubble_sort(arr):
    # Loop over the entire array, performing passes
    for i in range(len(arr) - 1):  # Outer loop for passes
        for j in range(len(arr) - 1 - i):  # Inner loop to compare adjacent items
            if arr[j] > arr[j + 1]:  # Compare adjacent items
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap if out of order
    return arr



from random import randint

num_array = []

for x in range(10):
    num_array.append(randint(1, 10))

print(num_array)

bubble_sort(num_array)
print(num_array)