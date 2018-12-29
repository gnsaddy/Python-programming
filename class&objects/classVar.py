class Employee:

    num_of_emp = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
          self.first = first
          self.last = last
          self.pay = pay
          self.email = first+"."+last + "@gmail.com"

          Employee.num_of_emp += 1
          
    def fullName(self):
        return '{} {}'.format(self.first, self.last)
  
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

print(Employee.num_of_emp) #before

emp_1 = Employee('aditya','raj',50000)
emp_2 = Employee('bhaskar','uday',60000)

print(Employee.num_of_emp) #after



# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

#only change in instance variable value 
# emp_1.raise_amount = 1.05
# emp_2.raise_amount = 1.06

# print(Employee.raise_amount)

# print(emp_1.__dict__)
# print(emp_2.__dict__)

# print(emp_1.pay)
# print(emp_2.pay)
# emp_1.apply_raise()
# emp_2.apply_raise()
# print(emp_1.pay)
# print(emp_2.pay)





