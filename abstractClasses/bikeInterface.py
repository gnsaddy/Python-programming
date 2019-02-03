from abc import ABC, abstractmethod

class VechicleInterface(ABC):

    @abstractmethod
    def companyName(self):
        pass

    @abstractmethod
    def model(self):
        pass

    @abstractmethod
    def vechicleState(self):
        pass


class Car(VechicleInterface):

    def companyName(self):
        print("--------Ford-------")

    def model(self):
        print("Model -- Ford Mastang model 2002 ")

    def vechicleState(self):
        print("Vechile state --- Karnataka ")



class Bike(VechicleInterface):

    def companyName(self):
        print("--------Honda-------")

    def model(self):
        print("Model -- Ford CBR 250 model 2018 ")

    def vechicleState(self):
        print("Vechile state --- Karnataka ")

class Truck(VechicleInterface):

    def companyName(self):
        print("--------Tata-------")

    def model(self):
        print("Model -- Tata Maxima model 2010 ")

    def vechicleState(self):
        print("Vechile state --- Delhi ")


objC = Car()
objB = Bike()
objT = Truck()

while(True):

    print("1- Car details \n2-Bike details \n3-Truck details")
    ch = int(input("Entet choice "))

    if ch == 1:
        objC.companyName()
        objC.model()
        objC.vechicleState()

    elif ch == 2:
        objB.companyName()
        objB.model()
        objB.vechicleState()

    elif ch == 3:
        objT.companyName()
        objT.model()
        objT.vechicleState()

    elif ch>3:
        print("Thank you for visit ")
        exit()
