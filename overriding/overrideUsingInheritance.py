# method overriding concept using inherit property
class Father:
    def phone(self):
        print("I have Nokia N73 ")

    def car(self):
        print("I have Maruti aulto 800 ")

    def house(self):
        print("I have my own house ")

class Son(Father):
    def phone(self):
        print("I have Motorola Z3 Phone ")

    def car(self):
        print("I have Renault Duster car ")

    def house(self):
        return super().house() # i don't have house so i inherit my father property so father house is my house

sonObj = Son()
sonObj.phone()
sonObj.car()
sonObj.house()

    
