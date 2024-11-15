def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j-1] > arr[j] and j > 0:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j-=1

    return arr



from random import randint

num_array = []

for x in range(10):
    num_array.append(randint(1, 10))

print(len(num_array))
print(num_array)

insertion_sort(num_array)
print(num_array)