# Defining a class
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

# Creating an object
my_car = Car("Toyota", "Camry")

# Accessing methods
my_car.display_info()
