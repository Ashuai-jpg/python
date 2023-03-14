#Polymorphism

class Animal:
    def __init__(self) -> None:
        print("Eating food")
        pass
    

class Cat(Animal):
    def eat():
        print("Eating cat food")
class Dog:
    def eat():
        print("Eating dog food")


Animal1 = Cat
Animal2 = Dog

Animal1.__init__(Animal)
Animal1.eat()
Animal2.eat()