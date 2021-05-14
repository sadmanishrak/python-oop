class Dog:

    # __init__ is called just like javascript constructor
    # name is an attribute that we can pass to the class
    def __init__(self, name, age): 
        self.name = name
        self.age = age
        # print(name)

    # The self below parameter passes the object from the previous __init__ method. Without the "self" parameter you will always get an error
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    # Here is a method to change age via a method. Here the age parameter is a must. Or else it will not be able to get the value to9 change the age to.
    def set_age(self, age):
        self.age = age

    # def add_one(self, x):
    #     return x + 1

    # def bark(self):
    #     print("bark")

# It is necessary that we pass the age attribute to the class. Without it we are going to get an error. Like "d = Dog("Tim")" will surely throw an error
d = Dog("Tim", 34)

# Accessing the attribute "name" from the class
print(d.name)

# Accessing the attribute "age" from the class
print(d.age)

d2 = Dog("Bill", 12)

# Accessing the attribute through a method of the class
print(d2.get_name())
print(d2.get_age())

# By calling the set_age method we are changing the value of age here.
d2.set_age(2)
print("This is the new age after calling method set_age: ", d2.get_age())


# d.bark()
# print(d.add_one(5))
# print(type(d))
