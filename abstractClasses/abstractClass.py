from abc import ABC
from abc import abstractmethod

class parent(ABC):
    @abstractmethod 
    def show(self):
        pass

    @abstractmethod
    def disp(self):
        pass
    def check(self):
        print("from abstract class")

class child1(parent):
    def show(self):
        print("Implementation of abstract method in first child class")

    def disp(self):
        print("implementation in first child class")

class child2(parent):
    def show(self):
        print("Show in second child class ")
    def disp(self):
        print("Display from class second ")

obj = child1()
obj.show()
obj.disp()
obj.check()

obj2 = child2()
obj2.show()
obj2.disp()
obj2.check()