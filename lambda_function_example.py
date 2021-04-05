# A lambda function can take any number of argument but only one expression
# A lambda function is a small anonymous(A function without name) function
# A Variable Name = (Lambda Keyword Arguments : Expresstion) (Argument Value)
result = (lambda x, y, z : x*y*z) (2, 5, 9)
print(result)

# We can do the same thing using function
def mul1(x, y, z):
    return x*y*z

result = mul1(2, 5, 9)
print(result)
