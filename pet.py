class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def get_status(self):
        return f"{self.name} - Hunger: {self.hunger}, Energy: {self.energy}, Happiness: {self.happiness} 🙈"

    def eat(self):
        self.hunger = max(0, self.hunger - 2)
        self.happiness += 1
        print(f"{self.name} ate and now feels happier! 🥰")

    def sleep(self):
        self.energy = min(10, self.energy + 3)
        print(f"{self.name} slept and is now more energized! 😴")

    def play(self):
        self.happiness += 2
        self.hunger += 1
        self.energy = max(0, self.energy - 1)
        print(f"{self.name} played and had fun, but got a bit hungry! 🐾")

    def train(self, trick):
        self.tricks.append(trick.capitalize())
        print(f"{self.name} learned the trick: {trick.capitalize()}! 🎓")
        self.hunger += 1
        self.energy = max(0, self.energy - 1)
        self.happiness += 1

    def show_tricks(self):
        print(f"{self.name} has learned the following tricks: {', '.join(self.tricks)} 🎩")
