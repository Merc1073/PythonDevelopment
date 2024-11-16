import numpy as np

# Create a 1D array
arr = np.array([1, 2, 3, 4, 5])
print(arr)

# Create a 2D array
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr_2d)

print(arr.shape)  # Shape of the array
print(arr.ndim)   # Number of dimensions
print(arr.dtype)  # Data type of elements


a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)  # Element-wise addition
print(a * b)  # Element-wise multiplication
print(a ** 2) # Element-wise exponentiation

print(a + 10)  # Add 10 to every element

zeros = np.zeros((3, 3))  # 3x3 matrix of zeros
ones = np.ones((2, 2))    # 2x2 matrix of ones

print(zeros)
print(ones)

random_numbers = np.random.rand(3, 3)  # Random numbers in [0, 1)
print(random_numbers)

identity = np.eye(3)  # 3x3 Identity matrix
print(identity)

print(arr[0])   # First element
print(arr_2d[0, 1])  # Element at first row, second column

print(arr[1:4])  # Elements from index 1 to 3

reshaped = arr.reshape((1, 5))  # Convert 1D array to 2D
print(reshaped)

combined = np.concatenate((a, b))
print(combined)

print(np.sum(arr))      # Sum of all elements
print(np.mean(arr))     # Mean of the array
print(np.max(arr))      # Maximum element

sorted_arr = np.sort(arr)
print(sorted_arr)



test_array = np.arange(1, 13)
reshaped = test_array.reshape(3, 4)
print(reshaped)

# for i in test_array:
#     for j in test_array:
#         test_array[i:j] = np.random.randint(1, 10)
