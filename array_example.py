from numpy import *
from numpy import array

array1 = array([
    [1,2,3,4,5,6],
    [7,8,9,5,4,3]
])
# Printing Array
print(array1)

# Printing Array Type
print(array1.dtype)

# Printing Array Dimension
print(array1.ndim)

# Printing Array Row Column Number
print(array1.shape)

# Printing Array Size
print(array1.size)

# Converting 2D array to 1D array
array2 = array1.flatten()
print(array2)

# Converting 1D array to 2D array
array3 = array2.reshape(2,6)
print(array3)

# Converting 1D array to 3D array
array4 = array2.reshape(2,2,3)
print(array4)