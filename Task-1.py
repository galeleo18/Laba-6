class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}")

BMW = Car("BMW", "Gran Turismo", 2021)
BMW.info()