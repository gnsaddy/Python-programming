class Animal:
    def __init__(self, name):
        self.name = name

    def talk(self):
        pass


class Dog(Animal):
    def talk(self):
        print(self.name , 'Woof!')

class Cat(Animal):
    def talk(self):
        print(self.name , 'MEOW!')
    
class Lion(Animal):
    def talk(self):
        print(self.name , "Roar!")


c = Cat('kitty')
c.talk()
d = Dog('Tommy')
d.talk()
l = Lion('Sheru')
l.talk()
