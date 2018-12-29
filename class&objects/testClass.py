class Employee:
    pass  # empty class so use pass to skip this class


#creating of instance of class
emp_1 = Employee() #instance of class employee
emp_2 = Employee() #instance of class employee

print(emp_1) #this print the employee object
print(emp_2)

#instance variable for emp_1

emp_1.first = "Aditya"
emp_1.second = "Raj"
emp_1.email = "gnsaddy@gmail.com"
emp_1.pay = 600000

#instance variable for emp_2

emp_2.first = "Bhaskar"
emp_2.second = "uday"
emp_2.email = "bhaskar@gmail.com"
emp_2.pay = 75000


print("employee name ", emp_1.first," " ,emp_1.second)
print("employee email", emp_1.email)
print("employee salary", emp_1.pay)

print("employee name ", emp_2.first, " ", emp_2.second)
print("employee email", emp_2.email)
print("employee salary", emp_2.pay)
