class Soda:
    def __init__(self, addition=None):
        self.addition = addition

    def show_my_drink(self):
        if self.addition:
            print(f"Газировка и {self.addition}")
        else:
            print("Обычная газировка")

add = input("Можете вввести добавку к газировке если желаете: ")
drink = Soda(add if add else None)
drink.show_my_drink()