class Nikola:
    __slots__ = ['name', 'age']

    def __init__(self, name, age):
        if name != "Николай":
            self.name = f"я не {name}, а Николай"
        else:
            self.name = name
        self.age = age

name = input("Введите имя: ")
age = int(input("Введите возраст: "))

person = Nikola(name, age)
print("Имя:", person.name)
print("Возраст:", person.age)