# Inheritance
# With inheritance you can inherit the properties and methods of a class in another class.
# Benefits of inheritance:
# 1. Code reuse
# 2. Extensibility
# 3. Readability
class Vehicle:
    def general_usage(self):
        print("general use: transporation")

class Car(Vehicle):
    def __init__(self):
        print("I am car")
        self.wheels=4
        self.has_roof=True

    def specific_usage(self):
        self.general_usage()
        print("specific use: commute to work, vacation with family")


class MotorCycle(Vehicle):
    def __init__(self):
        print("I'm motor cycle")
        self.wheels=2
        self.has_roof=False

    def specifc_usage(self):
        self.general_usage()
        print("specific use:road trips,racing")

c= Car()


m=MotorCycle()

#print(isinstance(c,MotorCycle))
#print(issubclass(Car,Vehicle))

#Exercise

class Animal():
    def habitat(self):
        print("This animal has a habitat")

class Dog(Animal):
    def habitat(self):
        Animal.habitat(self)
        print("The dog's habitat is a kennel")
a=Animal()
d= Dog()
d.habitat()
print(isinstance(a,Dog))
print(issubclass(Dog,Animal))
