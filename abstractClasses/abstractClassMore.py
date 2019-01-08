from abc import ABC, abstractmethod

class Main(ABC):
    @abstractmethod
    def name(self):
        pass
    
    @abstractmethod
    def address(self):
        pass

    @abstractmethod
    def showData(self):
        pass

class GiveName(Main):
    def name(self):
        self.fname = input("Enter first name : ")
        self.lname = input("Enter last name : ")
    def showData(self):
        return self.fname +" "+self.lname

class GiveAddress(GiveName):
    def address(self):
        self.addr = input("Enter address : ")
    def showData(self):
        print("Name : ", super().showData()) # super() for calling the super class method
        print("Address : ", self.addr)
        

addressObj = GiveAddress()
addressObj.name()
addressObj.address()
addressObj.showData()
