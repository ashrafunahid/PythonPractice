n = int(input("How many Chocolate do you need?"))
available = 5
i=1

while i<=n:
    if i>available:
        print("Not Available.")
        break
    print("Available", i)
    i+=1