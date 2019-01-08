# overriding of methods
class PYCharm:
    def execute(self):
        print("Compiling")
        print("Running")

class VSCode:
    def execute(self):
        print("Compiling")
        print("Running")
        print("Text Editor")
        print("Coding Conventions")

class Laptop:
    def code(self,ide):
        ide.execute()

ide1 = PYCharm()
ide2 = VSCode()     

lap1 = Laptop()
# lap1.code(ide1)
lap1.code(ide2)
