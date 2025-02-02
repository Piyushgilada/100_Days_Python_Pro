class Animal:
    def __init__(self):
        self.num_eyes=2

    def breathe(self):
        print("Inhale, exhale.")

class Fish(Animal):
    def __init__(self):
        super().__init__()
    def swim(self):
        print("moving in water")

    def breathe(self):
        super().breathe()
        print("doing underwater")

fish=Fish()
fish.breathe()
fish.swim()
print(fish.num_eyes)