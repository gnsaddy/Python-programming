#python class constructor 
# __init__() method

class Employee:

    def __init__(self, first, last, pay ):
          self.first = first
          self.last = last
          self.pay = pay
          self.email = first+"."+last+ "@gmail.com"
    
    def fullName(self):
        return '{} {}'.format(self.first, self.last)
        

emp_1 = Employee('aditya','raj',60000)
emp_2 = Employee('bhaskar','uday',75000)

print(emp_1.email)
print(emp_2.email)

# format method used to format the output
print('{} {} {}'.format("employee name = ",emp_1.first, emp_1.last))

#function call
print(emp_1.fullName())
# use can also use like
print(Employee.fullName(emp_2))