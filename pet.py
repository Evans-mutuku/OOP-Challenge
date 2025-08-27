class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5  # Medium hunger
        self.energy = 5  # Medium energy
        self.happiness = 5  # Medium happiness
        self.tricks = []  # Empty list for tricks

    def eat(self):
        self.hunger = max(0, self.hunger - 3)  # Ensure hunger doesn’t go below 0
        self.happiness = min(10, self.happiness + 1)  # Ensure happiness doesn’t exceed 10
        print(f"{self.name} ate food. Hunger: {self.hunger}, Happiness: {self.happiness}")

    def sleep(self):
        self.energy = min(10, self.energy + 5)  # Ensure energy doesn’t go above 10
        print(f"{self.name} slept. Energy: {self.energy}")

    def play(self):
        self.energy = max(0, self.energy - 2)  # Reduce energy but not below 0
        self.happiness = min(10, self.happiness + 2)  # Increase happiness but not above 10
        self.hunger = min(10, self.hunger + 1)  # Increase hunger but not above 10
        print(f"{self.name} played! Energy: {self.energy}, Happiness: {self.happiness}, Hunger: {self.hunger}")

    def get_status(self):
        print(f"{self.name}'s Status ➡ Hunger: {self.hunger}, Energy: {self.energy}, Happiness: {self.happiness}")

    def train(self, trick):
        self.tricks.append(trick)  # Add trick to the list
        print(f"{self.name} learned a new trick: {trick}!")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows these tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")