from abc import ABC,abstractmethod

class Test(ABC):

    def __hidden(self):
        print("Hidden method but relevent")
    
    def __hidden2(self):
        print("Hidden method but not relevent")

    def hidden(self):
        self.__hidden()

    def hidden2(self):
        self.__hidden2()

    @abstractmethod
    def funcAbstract(self):
        pass

class Show(Test):

    def funcAbstract(self):
        print("Relevent data ")
        return super().hidden()

obj = Show()
obj.funcAbstract()
        


