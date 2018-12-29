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

    @classmethod
    def cls_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        

# print(Employee.num_of_emp) #before
emp_1 = Employee('aditya','raj',50000)
emp_2 = Employee('bhaskar','uday',60000)

# print(Employee.num_of_emp) #after

# Employee.cls_raise_amt(1.08)

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)







