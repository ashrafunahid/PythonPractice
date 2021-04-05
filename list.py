# List is a ordered collection which is changeable
# List allow duplicate values
# List represented in []
# It has no issues with data type, any type of data type is allowed
# It Need higher memory size then tuple
list = [1, 'Ashraf', 3, 7, 3, 9]
print(list)

# Can be check with location
print(list[1])

# Can be use nested list
# Here whole nested list will count as an index
list2 = [3, 5 , 9, ['Ashraf', 'Ohi'], 3, 9]
print(list2)

# Here ['Ashraf', 'Ohi'] index is list2[3]
print(list2[3])

# List can be extended with a built in function
list.extend(['Tahia'])
print(list)

# List can be extended with normal + sign
list = list + ['Ohi']
print(list)

# List can remove any value
list.remove(7)
print(list)

# List can remove any value using index
list.remove(list[4])
print(list)

# List can count that how many times a value is stored
print(list.count(3))