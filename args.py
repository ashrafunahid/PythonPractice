def myFunc(arg):
    print(arg)

myFunc('This is Function Argument')

# Multiple argument
def myFunc1(*arg):
    for i in range(1,*arg):
        print(i)

myFunc1(10)