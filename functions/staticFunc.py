class Calc:


    @staticmethod 
    def sum(x,y):
        print("sum =",x+y)

    @staticmethod
    def sub(x,y):
        print("sub=",x-y)

    @staticmethod
    def mul(x,y):
        print("mul=",x*y)



ch = int(input("enter choice"))

while ch:

    if ch==1:
        Calc.sum(30,40)
        break

    if ch==2:
        Calc.sub(40,20)
        break

    if ch==3:
        Calc.mul(12,23)
        break
