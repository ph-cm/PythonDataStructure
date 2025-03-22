#Class is a blueprint for creating objects. It defines attributes (data) and methods (functions) that the object will have == MOLDE

#Class describes what a dog should have(attributes) and what a dog should do (method)
class Dog:
    def __init__(self, name, age): #Construtor
        self.name = name #attribute
        self.age = age #attribute
    
    def bark(self):
        print(f"{self.name} says woof!")
        
#Creating an object based on the Dog class
my_dog = Dog("Jade", 12)
my_dog.bark()