s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = {4, 5, 6}

# Finding common values between two sets
print(s1.intersection(s2))

# Finding difference between two sets
# s1.difference(s2) Here s2 is main and s1 is sub
print(s1.difference(s2))

# Excluding duplicate values
print(s1.symmetric_difference(s2))

# Converting List into Set
a={1, 2, 3, 4, 3, 4, 5}
print(set(a))

# Converting List into set and again into List
a={1, 2, 3, 4, 3, 4, 5}
print(list(set(a)))