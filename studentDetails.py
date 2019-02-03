import csv

class Student:

    def getDetails(self):
        self.name = input("Enter name : ")
        self.USN = input("Enter USN : ")
        self.marks = input("Enter marks :")
        self.age = input("Enter age : ")

    def getCurricular(self):
        self.sports = input("Enter sports activity : ")
        self.coding = input("Enter coding activity : ")
        self.extra = input("Enter Extra co-curricular acticity : ")

class Display(Student):

    def address(self):
        self.address=input("Enter address : ")

    def show(self):
        print("Name : ", self.name)
        print("USN : ", self.USN)
        print("Marks : ", self.marks)
        print("age : ", self.age)
        print("Address : ", self.address)
        print("Sports : ", self.sports)
        print("Coding : ", self.coding)
        print("extra : ", self.extra)

    
obj  = Display()
obj.getDetails()
obj.getCurricular()
obj.address()
obj.show()
dt = obj.__dict__

with open("data.txt",'w') as f:
    f.write(str(dt))

w = csv.writer(open("output.csv", "w"))
for key, val in dt.items():
    w.writerow([key, val])

