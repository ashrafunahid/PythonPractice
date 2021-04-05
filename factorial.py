# Finding Factorial of 5 using Math function
import math
print('The Factorial value of 5 is: ',math.factorial(5))

# Finding Factorial of 5 using function
def factorial(n):
    a = 1
    for i in range(1,n+1):
        a = i*a
    print('The Factorial value of 5 is: ',a)

factorial(5)

# Finding Factorial of 5 without function
a = 1
for i in range(1, 6): #Range function uses n-1 concept for last value
    a = i*a
print('The Factorial value of 5 is: ',a)

# Finding Factorial of 5 using while loop
fact = 5
a = 1
i = 1
while i<=fact:
    a = a*i
    i = i+1
print('The Factorial value of 5 is: ',a)
