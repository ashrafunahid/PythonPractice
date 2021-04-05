a = 5
b = 10
print('A=',a,'\n','B=',b)

# We can swap the value
a, b = b,a
print('A=',a,'\n','B=',b)

# In another way
temp = a
a = b
b = temp
print('A=',a,'\n','B=',temp)