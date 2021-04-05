num = int(input("Please enter a number: "))

for i in range(2, num):
    if num%i ==0:
        print("Not a prime number")
        break
else:
    print("Oh It's prime number")