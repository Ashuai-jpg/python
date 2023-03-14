# Operator Overloading

class Dog:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        pass
    def __gt__(self, other): #this is the operator overloading to greater than '>'
        return "yes" if self.age > other.age else "no"
    def __lt__(self, other): #this is the operator overloading to less than '<'
        return "确实小啊" if self.age < other.age else "确实老啊"
Guy = Dog("Guy_z", 22)
Zhang = Dog("ZZB", 23)

print(Guy > Zhang) #invoke the '__gt__()' function in class Dog
print(Guy < Zhang) #invoke the '__lt__()' function in class Dog