from abc import ABC,abstractmethod

class Main(ABC):
    def __init__(self,val1,val2): #local var val1 ,val2
        self.val1 = val1  # making class variable
        self.val2 = val2  # making class variable

    def display(self):
        pass

class Add(Main):
    def display(self):
        print("First number : ", self.val1)
        print("Second number : ", self.val2)
        print("Sum : ", self.val1 + self.val2)

class Mul(Main):
    def display(self):
        print("First number : ", self.val1)
        print("Second number : ", self.val2)
        print("Sum : ", self.val1 * self.val2)

objAdd = Add(10,22)  # passing parameter 
objMul = Mul(10, 20)  # passing parameter

objAdd.display()
objMul.display()
