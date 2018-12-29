class Test:
    _var1 = 10 # pretend to be a protected 
    __var2 = 20 # private variable

    def disp(self):  #public method
        print(self._var1)
        print(self.__var2)

obj = Test()
obj.disp()  # shows the public and protected data
# print(obj._var1)
# print(obj._Test__var2)


class Robot(object):
   def __init__(self):
      self.__version = 22

   def getVersion(self):
      print(self.__version)

   def setVersion(self, version):
      self.__version = version


obj = Robot()
obj.getVersion()
obj.setVersion(23)
obj.getVersion()
print(obj.__version)
