import sys
# Touple is a ordered collection which is unchangeable
# Touple allow duplicate values
# Touple represented in ())
# It has no issues with data type, any type of data type is allowed
# It Need lower memory size then list
tuple = (0, 8, 'Ashraf', 9, 45)
print(tuple)

# Values of tuple can't be remove but whole tuple can be delete
del tuple
print(tuple)

# Size of list or tuple can be count
# # For this we need to import sys
tuple2 = (0, 8, 'Ashraf', 9, 45, 'Tahia', 'Ohi')
print('This tuple size in Memory is:', sys.getsizeof(tuple2))