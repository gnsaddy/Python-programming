# python have two types of variable 
# class variable or static variable
# instance variable

class College:
    ''' College name for every student of a college is same '''
    ''' Class/static method are common for all '''

    collegeName = "RV College of Engineering"
    collegeTiming = ("9 am to 4 pm")

    def studentDetails(self,name,department):
        self.name = name
        self.department = department

    def display(self):
        print('Name {} \nTiming {} \nDepartment {} \nCollege Name {}  '.format(self.name,self.collegeTiming,self.department,self.collegeName))

stu1 = College()
stu2 = College()
stu1.studentDetails('Aditya Raj','MCA')
stu2.studentDetails('Bhaskar Uday', 'Btech')
stu1.display()
print("------------------")
stu2.display()

