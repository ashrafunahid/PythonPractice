# Set is almost like list and tuple
# Difference is set not support duplicate values
# Set normally uses in {}
list = [0, 1, 2]
s1 = set(list)
print(s1)

# We can add a single value to set
s1.add(3)
print(s1)

# We can add multiple value to set using update function
s1.update([4, 5, 6])
print(s1)

s2 = {7, 8}
s1.update(s2)
print(s1)

s3 = {11, 12}
s1.update([9, 10],s3)
print(s1)

# We can remove a single value from set but value must have to available in set
s1.remove(12)
print(s1)

# Can be remove a value if it is not available in set
s1.discard(13)
print(s1)