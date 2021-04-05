# Dictionary is a collection which is unordered, changeable and indexed
# Index should be unique but can be any data type (Int, Float, String..)
# Represented in {}
dictionary = {'Name': 'Ashraf', 'Age': 28, 'Address': 'Dagonbhuiyan'}
print(dictionary)

# Here value can be same but index should be unique
dictionary2 = {'Name': 'Ashraf', 'Age': 28, 'Age2':28, 'Address': 'Dagonbhuiyan'}
print(dictionary2['Age2'])

# Dictionary index can be used with get function
print(dictionary2.get('Age2'))

# Dictionary index can be check with keys function
print(dictionary.keys())

# Dictionary Item can be found with items function
print(dictionary.items())

# Dictionary can be copy another dictionary
dictionary3 = dictionary.copy()
print(dictionary3)

# Items can be added in dictionary
dictionary['Height'] = '63inch'
print(dictionary)

# Single item can be remove from dictionary
dictionary.pop('Height')
print(dictionary)

# Dictionary can be cleared
dictionary2.clear()
print(dictionary2)

# Dictionary can be delete
del dictionary2
# print(dictionary2)