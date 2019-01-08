'''Polymorphism with Inheritance:
In Python, Polymorphism lets us define methods in the child class 
that have the same name as the methods in the parent class. 
In inheritance, the child class inherits the methods from the parent class.
 However, it is possible to modify a method in a child class 
 that it has inherited from the parent class. 
This is particularly useful in cases where the method inherited from the parent class 
 doesn’t quite fit the child class. In such cases, we re-implement the method in the child class. 
This process of re-implementing a method in the child class is known as Method Overriding.'''


class Bird:
    def intro(self):
        print("There are many types of birds.")
        
    def flight(self):
        print("Most of the birds can fly but some cannot.")


class sparrow(Bird):
    def flight(self):
        super().intro()
        print("In which Sparrows can fly.") 


class ostrich(Bird):
    def flight(self):
        print("But Ostriches cannot fly.")


obj_spr = sparrow()
obj_ost = ostrich()

obj_spr.flight()
obj_ost.flight()
