#Properties: Allow controlled access to attibutes
#Decorators: Modify the behvior of functions or methods
#Context Managers: Manage resources using with statements

#Properties
class Circle:
    def __init__(self, radius):
        self._radius = radius #Privvate attribute 
    
    #Getter
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value > 0:
            self._radius = value
        else:
            raise ValueError("Radius must be positive")
        
my_circle = Circle(5)
print(my_circle.radius)
my_circle.radius = 10
print(my_circle.radius)