a = int(input("Please Enter First Number: "))
b = int(input("Please Enter Second Number: "))
c = int(input("Please Enter Third Number: "))

if a>b:
    if a>c:
        print("First number is Greater")
    else:
        print("Third Number is Greater")
elif b>a:
    if b>c:
        print("Second Number is Greater")
    else:
        print("Third Number is Greater")
