# Define a class Animal and another class Dog that inherits from Animal.


class Animal:
    def __init__(self,name): # Animal എന്ന ക്ലാസിന്റെ constructor
        self.name = name     # name എന്ന attribute സെറ്റ് ചെയ്യുന്നു

        
    def speak(self):
        print(f"{self.name} makes a sound.")  # speak() method: "Animal sound" print ചെയ്യുന്നു
        
 # Derived class
# Dog is a derived (child) class that inherits from Animal.
# It overrides the speak() method to give a specific message for dogs.

       
class Dog(Animal):
    def speak(self):
        print(f"{self.name} says Woof!")
        
        
a = Animal("Generic Animal")
a.speak()  # Output: Generic Animal makes a sound.

d = Dog("Tommy")
d.speak()  # Output: Tommy says Woof!

