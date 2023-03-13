#Classes
class Animal:
    def __init__(self) -> None:
        pass
    def walk(self):
        print("walking")

class Dog(Animal):
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        pass
    def bark(self):
        print("Woof!")


playBog = Dog("PlayBog", 1.5)

print(playBog.name)
print(playBog.age)

playBog.bark()
playBog.walk()

