number1 = int(input("Please Enter First Number: "))
number2 = int(input("Please Enter Second Number: "))
number3 = int(input("Please Enter Third Number: "))

if number1>number2 and number1>number3:
    print("First Number is Greater")
elif number1<number2 and number2>number3:
    print("Second Number is Greater")
elif number3>number2 and number3>number1:
    print("Third Number is Greater")

if number1>number2 or number1>number3:
    print("First Number is Greater")