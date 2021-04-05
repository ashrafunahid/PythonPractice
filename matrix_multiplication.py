import numpy as np

m1 = (
    [1,2,3],
    [4,5,6],
    [7,8,9]
)

m2 = (
    [7,8,9],
    [4,5,6],
    [1,2,3]
)

# We can add two matrix
result = np.add(m1, m2)
print('Addition of two matrix: ')
print(result)

# We can Subtruction between two matrix
result = np.subtract(m1, m2)
print('Subtruction of two matrix: ')
print(result)

# We can multiply two matrix
# 1*7 + 2*4 + 3*1 = 7+8+3 = 18
result = np.dot(m1, m2)
print('Multiplication of two matrix: ')
print(result)

# We can multiply tow matrix using index
result = np.multiply(m1, m2)
print('Index Multiplication of two matrix: ')
print(result)