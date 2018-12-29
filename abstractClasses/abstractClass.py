from abc import ABC
from abc import abstractmethod

class parent(ABC):
    @abstractmethod 
    def show(self):
        pass

class child(parent):
    def show(self):
        print("Implementation of abstract method in child class")

obj = child()
obj.show()