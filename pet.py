class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    # reduces hunger by 3 points (but not below 0), and increases happiness by 1.
    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} is eating!")

    # increases energy by 5 points (but not above 10).
    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} is sleeping!")

    # decreases energy by 2, increases happiness by 2, and increases hunger by 1.
    def play(self):
        if( self.energy <= 0):
            print(f"{self.name} is tired!")
            return
        else:
            self.energy = max(0, self.energy - 2)
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.name} is playing...")

    # that teaches your pet a new trick and stores it in a list.
    def train(self, trick):
        self.tricks.append(trick)
        # print(f"{self.name} is learning a new trick: {trick}")

    def show_tricks(self):
        print(f"{self.name} knows these tricks: {self.tricks}")

    # prints the current state of the pet.
    def get_status(self):
        print(f"\n{self.name}'s Status:")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")









