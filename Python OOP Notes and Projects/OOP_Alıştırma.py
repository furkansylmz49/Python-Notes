class Animal:
    def __init__(self,age):
        self.age = age

    def __str__(self):
        return f"Animal is {self.age} years old."

class Dog(Animal):
    def __init__(self,age,foot):
        super().__init__(age)
        self.foot = foot

    def __str__(self):
        return f"Animal is {self.age} years old. \nAnimal have {self.foot} foot."

    def dog(self):
        print("Hav Hav Hav")

class Cat(Animal):
    def __init__(self,age,foot):
        super().__init__(age)
        self.foot = foot

    def __str__(self):
        return f"Animal is {self.age} years old. \nAnimal have {self.foot} foot."

    def cat(self):
        print("Miyav Miyav")


cat1 = Cat(1,4)
cat2 = Cat(4,4)
dog1 = Dog(5,4)

#del cat1.age
#print(cat1.age)

print(isinstance(dog1,Dog))
print(isinstance(dog1,Cat))
print(isinstance(dog1,Animal))
print()
print(issubclass(Dog,Dog))
print(issubclass(Dog,Cat))
print(issubclass(Dog,Animal))
print()
print(cat1,"\n")
print(cat2,"\n")
print(dog1)