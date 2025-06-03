class KgToPounds:
    def __init__(self, kg):
        self.__kg = kg

    @property
    def kg(self):
        return self.__kg

    @kg.setter
    def kg(self, value):
        self.__kg = value

    def to_pounds(self):
        return self.__kg * 2.20462

kg = float(input("Введите вес в киллограммах: "))
weight = KgToPounds(kg)
print("Вес в фунтах:", weight.to_pounds())