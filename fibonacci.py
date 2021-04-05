# Finding Fibonacci Series of 10 using Function
def fibonacci(args):
    a = 0
    b = 1
    for i in range(2, args):
        c = a+b
        a = b
        b = c
        print(c)
fibonacci(10)

# Finding Fibonacci Series of 10 without function
a = 0
b = 1
for i in range(2, 10):
    c = a+b
    a = b
    b = c
    print(c)