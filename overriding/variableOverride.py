#overriding of variable 

class Parent:
    havingCar = "Alto 800"
    havingBike = "Hero Splender"

class Child(Parent):
    havingCar = "Suzuki Baleno"
    havingBike = "Bajaj Dominor"
    #if overriding then child varible is executed

class Child2(Parent):
    pass
    # if not overriding then parent class variable is executed

childObj = Child()
print(childObj.havingCar, " ", childObj.havingBike)
child2Obj = Child2()
print(child2Obj.havingCar, " ", child2Obj.havingBike)
