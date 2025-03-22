#In python 3, all classes are new style classes by defauld(they inherit from object).
# New-style classes support features like descriptors, properties and the super() function

class MyClass(object): #Explicity inheriting from 'object' that is the base class for all classes in Python
    def __init__(self, value):
        self.value = value
    
    def display(self):
        print(f"Value: {self.value}")
        
obj = MyClass(10)
obj.display()

# Object class provides default implementations for common methods that all objects in Python should have. These methods are part of the Python data model and allow 
# the objects to interact with Python's build in features

# A classe can inherit more than one class so it can have access to all the methods and attributes from both other inherit classes
#Em Python, métodos de instância devem ter self como o primeiro parâmetro. O self é uma referência à instância da classe e permite acessar atributos e outros métodos da classe
class A():
    def __init__(self, value_A):
        self.value_A = value_A
        
    def method_A(self):
        print("A")
    
class B():
    def __init__(self, value_B):
        self.value_B = value_B
        
    def method_B(self):
        print("B")
        
class C(A, B):
    def __init__(self, value_A, value_B):
        A.__init__(self, value_A)
        B.__init__(self, value_B)
                
    def sum(self):
        print(self.value_A + self.value_B)
        
    def method_C(self):
        print("C")

obj = C(10, 30)
obj.method_A()
obj.method_B()
obj.method_C()
obj.sum()