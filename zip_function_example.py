name = ['Nahid', 'Nadim', 'Nahin', 'Nakib']
age = [30, 28, 20, 9]

# We can combine two list using zip function and show the value after converting in list
combine_data = list(zip(name, age))
print(combine_data)

# We can add a new list to zip
combine_data = list(zip('1234', name, age))
print(combine_data)

# Unzip Example
all_data = [('1', 'Nahid', 30), ('2', 'Nadim', 28), ('3', 'Nahin', 20), ('4', 'Nakib', 9)]

# We can unzip a list using zip function
# There is no unzip function
# We need to use zip function to unzip a list
# Just we Need to use a * mark before list name
unzip_data = list(zip(*all_data))
print(unzip_data)

# We can unzip list using index name
serial = unzip_data[0]
print(serial)

name = unzip_data[1]
print(name)

age = unzip_data[2]
print(age)