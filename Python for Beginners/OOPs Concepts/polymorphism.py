class Bird:
    def make_sound(self):
        print("Some bird sound")

class Sparrow(Bird):
    def make_sound(self):
        print("Chirp Chirp")

class Parrot(Bird):
    def make_sound(self):
        print("Squawk")

# Function demonstrating polymorphism
def sound_of_bird(bird):
    bird.make_sound()

# Different behaviors with same method
sound_of_bird(Sparrow())  # Output: Chirp Chirp
sound_of_bird(Parrot())   # Output: Squawk
