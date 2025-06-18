class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 3
        self.energy = 7
        self.happiness = 8
        self.tricks = []

    def eat(self):
        self.hunger = max(0, self.hunger - 2)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} ate some meal!")

    def sleep(self):
        self.energy = min(10, self.energy + 7)
        print(f"{self.name} had a nice nap!")

    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(10, self.happiness + 8)
            self.hunger = min(10, self.hunger + 2)
            print(f"{self.name} played happily!")
            return
        else:
            print(f"{self.name} is too tired to play.")
            
    def train(self, trick):
        if self.energy_level > 2:
            print(f"{self.name} is too tired to learn a new trick!")
            return
    def train(self, trick):
        self.tricks.append(trick)
        print(f"{self.name} learned a new trick: {trick}!")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows the following tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} doesn't know any tricks yet.")

    def get_status(self):
        print(f"Status of {self.name}:")
        print(f"  Hunger: {self.hunger}/10")
        print(f"  Energy: {self.energy}/10")
        print(f"  Happiness: {self.happiness}/10")
