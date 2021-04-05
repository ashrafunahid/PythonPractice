# Recursion is a function that can be called from itself
# Recursion will act as infinite loop, but the default looping time is 1000
import sys
print('Normal Recursion Limit is: ', sys.getrecursionlimit())

# We can modify the looping time
sys.setrecursionlimit(1500)

# Example
# count = 0
# def MyFunc():
#     global count
#     count = count+1
#     print('Good Day', count)
#     MyFunc()
# MyFunc()

# Finding Factorial Value of a Number using Recursion

def MyFact(x):
    if x==0:
        return 1
    return x*MyFact(x-1)

result = MyFact(6)
print('Factorial value is: ', result)
