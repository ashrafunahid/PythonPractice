def mul_with_five(number):
    return number * 5

result = []
num = [15, 20, 25, 30, 35]
for i in num:
    result = mul_with_five(i)
    print(result)

# We can do the same thing using map function
# Map Function is a function which can take another function and iterable object as arguemnt
def mul_with_five(number):
    return number * 5
num = [15, 20, 25, 30, 35]
result = list(map(mul_with_five, num))
print(result)
