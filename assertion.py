def MySalary(salary):
    assert salary > 0, 'Salary can not be less then zero'
    print("My Salary is: ", salary, 'TK')

MySalary(int(input("Please Enter your Salary: ")))