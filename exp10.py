import numpy as np

# Create a 1D array with 9 random integers from 1 to 99
array = np.random.randint(1, 100, 9)

print("Original Array:")
print(array)

# Find square root of each element
print("\nSquare Root of Array:")
print(np.sqrt(array))

# Find number of dimensions
print("\nNumber of Dimensions:")
print(array.ndim)

# Reshape 1D array into 3x3 array
new_array = array.reshape(3, 3)

print("\n3 x 3 Reshaped Array:")
print(new_array)

# Find number of dimensions after reshaping
print("\nNumber of Dimensions after Reshape:")
print(new_array.ndim)

# Convert 2D array into 1D array
print("\nRavelled Array:")
print(new_array.ravel())

# Reshape again
newm = new_array.reshape(3, 3)

print("\nNew Matrix:")
print(newm)

# Slicing - row 3, columns 2 and 3
print("\nnewm[2,1:3]:")
print(newm[2, 1:3])

# Slicing - row 2, columns 2 and 3
print("\nnewm[1:2,1:3]:")
print(newm[1:2, 1:3])

# Slicing - rows 1 to 3, no columns
print("\nnew_array[0:3,0:0]:")
print(new_array[0:3, 0:0])

# First two rows, first column
print("\nnew_array[0:2,0:1]:")
print(new_array[0:2, 0:1])

# All three rows, first column
print("\nnew_array[0:3,0:1]:")
print(new_array[0:3, 0:1])

# Rows 2 and 3
print("\nnew_array[1:3]:")
print(new_array[1:3])