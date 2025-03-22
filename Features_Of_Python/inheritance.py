# Inheritance allows a class to inherit attributes and methods from another class. Te new class is called a subclass
# and dthe existing class is the superclass
# This allow us to abstract some general attributes and methods that we whould use in a lot of classes individualy

class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} make a sound")
        
class Cat(Animal):
    def speak(self):
        print(f"{self.name} make meow")
    
my_cat = Cat("Julie")
my_cat.speak()

my_dog = Animal("Jade")
my_dog.speak()