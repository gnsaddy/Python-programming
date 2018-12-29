# classmethod
class Animal:
    legs = 4  #common for all 

    @classmethod
    def walk(cls,name):
        print('{} walks with {} legs'.format(name,cls.legs))

Animal.walk('Dog')
Animal.walk('Cat')

# object count using classmethod
class Test:
    count = 0
    def __init__(self):
        Test.count = Test.count+1

    @classmethod
    def getNoOfobject(cls):
        print('Number of object created:', Test.count)

t1=Test()
t2=Test()
t3=Test()
t4=Test()
Test.getNoOfobject()

# staticmethod
class Teststatic:
    x=10
    y=20
    @staticmethod
    def sum():
        print("sum is ", Teststatic.x+Teststatic.y)
    @staticmethod
    def sub(a,b):
        print('sub is', a-b)


Teststatic.sum()
Teststatic.sub(20,10)





                                                                                       
