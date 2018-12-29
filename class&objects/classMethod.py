class First:
    message = "class message"

    @classmethod
    def cfun(cls):
        print("from the class method", cls.message)

    def ifun(self,newMsg):
        self.newMsg = newMsg
        # print(self.message)
        print("from the instance method ", newMsg)


First.cfun()  # class calling classmethod

obj = First()
obj.ifun('Instance call')
First.ifun(obj, 'Class call')
# obj.cfun()  # object calling classmethod

