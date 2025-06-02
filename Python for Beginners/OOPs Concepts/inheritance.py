# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

# Child class
class Dog(Animal):
    def speak(self):
        print(f"{self.name} says Woof!")

# Creating an object of Dog class
pet = Dog("Buddy")
pet.speak()
