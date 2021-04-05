a = int(input("Please enter First Number: "))
b = int(input("Please enter Second Number: "))


try:
    result = a/b
    print("Division result is:", result)

# # Here Exception is super Exception
# except Exception as e: #Here e is for Exception Message
#     print("Devide by Zero is not supported", e)

# We can use separate exception
except ZeroDivisionError:
    print("Devide by zero is not supported")
except ValueError:
    print("Please enter correct input")

finally:
    print("Thank You!")