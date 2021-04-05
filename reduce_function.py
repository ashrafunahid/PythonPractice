import functools
def series_summation(num1, num2):
    return num1+num2

list1 = [1,2,3,4,5,6,7,8,9]
result = functools.reduce(series_summation, list1)
print(result)