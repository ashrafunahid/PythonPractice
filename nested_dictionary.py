student = {
    1:{'Name': 'Ashraf Uddin', 'Age': 28, 'Address': 'Feni'},
    2:{'Name': 'Arif Uddin', 'Age': 26, 'Address': 'Dhaka'},
    3:{'Name': 'Aftab Uddin', 'Age': 18, 'Address': 'Chittagong'},
}
print(student)

# We can check with specific index
print(student[3]['Address'])

# We can add more index
student[4] = {} #First we need to declare parent index and assign it as blank
student[4]['Name'] = 'Atahar Uddin'
student[4]['Age'] = 10
student[4]['Address'] = 'Dhaka'
print(student)

# We can delete Specific Index
del student[4]['Address']
print(student)