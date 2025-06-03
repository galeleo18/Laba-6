class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Name: {self.name}, Age: {self.age}")

    def Speak(self):
        pass

class Dog(Animal):
    def Speak(self):
        print("Sharik govorit, RAF")

class Cat(Animal):
    def Speak(self):
        print("Murzik govorit, MUR")

dog = Dog("Sharik", 1)
dog.info()
dog.Speak()
cat = Cat("Murzik", 1)
cat.info()
cat.Speak()