# Inheritance
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old\n")

    def speak(self):
        print("I don't know what to say")

class Cat(Pet): # Inheriting the Pet class
    def __init__(self, name, age, color):
        super().__init__(name,age) # Doing the same as what the super() does in JavaScript
        self.color = color
    
    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old adn I am {self.color}\n")

class Dog(Pet): # Inheriting the Pet class
    def speak(self):
        print("Bark")

class Fish(Pet):
    pass

P = Pet("TIM", 19)
P.show()

C = Cat("Bill", 34, "Blue")
C.show() # We can do this here because Cat class has inherited from Pet class. This one also has an extra property of color.

D = Dog("Jill", 30)
D.show() # We can do this here because Cat class has inherited from Pet class

F = Fish("Bubbles", 10)
F.speak() # This one is coming from the Pet class as the Fish class does not have any method classed speak()
