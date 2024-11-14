# OOP = a programming paradigm, letting you structure code around "objects",
#       which are instances of classes.


# creating a class
class Cat:

    # constructor, is called when you create an object from this class,
    # allowing you to give this object values upon creation
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    # a method (function) inside of class
    def meow(self):
        print(f"{self.name} says Meow!")


# creating an instance (object) from our class
my_cat = Cat("Kripsy", "Siamese")

# calling a method created in class
my_cat.meow()



# Encapsulation = restricting access to data from outside of class

class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited: {amount}.")

    def get_balance(self):
        return self._balance


account = BankAccount()
account.deposit(100)
print(account.get_balance())





# Inheritance = creating a new class based on an existing class.
#               The new class inherits all attributes and methods from parent class.


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a noise.")


class Dog(Animal):
    def speak(self):
        print(f"{self.name} Woofs!")


animal1 = Animal("Fish")
animal1.speak()

dog1 = Dog("Junior")
dog1.speak()




# Polymorphism = allows objects of different classes to be
#                treated as objects of a common superclass


class Cat(Animal):
    def speak(self):
        print(f"{self.name} Meows!")

def animal_sound(animal):
    animal.speak()

cat1 = Cat("Chip")

animal_sound(dog1)
animal_sound(cat1)



# Abstraction = hides complexity of certain functions


from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)


circle1 = Circle(5)

print(circle1.area())