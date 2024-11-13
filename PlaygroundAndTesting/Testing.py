def bubble_sort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - 1 - i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array


from random import randint

num_array = []

for x in range(10):
    num_array.append(randint(1, 10))

print(len(num_array))
print(num_array)

bubble_sort(num_array)
print(num_array)