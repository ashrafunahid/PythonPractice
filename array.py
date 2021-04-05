from array import *
# Signed Integer 'i', Unsigned Integer 'I', Float 'f', double 'd'
salary = array('i', [223423, 4234234, 234234, 234234])

# Printing certain array
print(salary[1])

print('\n')

# Printing all array
for i in salary:
    print(i)

print('\n')

for i in range(4):
    print(salary[i])

# Memory info + Array Length
print(salary.buffer_info())

# Add a value to array
salary.append(429384)
print(salary)

# Remove a value from Array
salary.remove(234234)
print(salary)

# Show Reversed value in array
salary.reverse()
print(salary)