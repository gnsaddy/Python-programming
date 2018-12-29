# static method in a class
# python 2 syntax
class Sum:
    def addNum(x,y):
        return x+y
Sum.addNum = staticmethod(Sum.addNum)
print("sum is ", Sum.addNum(45,85))


        