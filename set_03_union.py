a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
c = {5, 6, 7, 8}

# Set Union
z = a.union(b)
print(z)

# Multiple Set Union
z = a.union(b,c)
print(z)

# Set union without using union function
z = a|b|c
print(z)