class Pet:
    def __init__(self, name: str, hunger: int = 5, energy: int = 5, happiness: int = 5):
        self.name = name
        self.hunger = hunger
        self.energy = energy
        self.happiness = happiness
        self.tricks = []

    def __str__(self):
        return f"{self.name} - Hunger: {self.hunger}, Energy: {self.energy}, Happiness: {self.happiness}"

    def eat(self):
        if self.hunger >= 3:
            self.hunger -= 3
        else:
            self.hunger = 0

        if self.happiness < 10:
            self.happiness += 1

    def sleep(self):
        if self.energy <= 5:
            self.energy += 5
        else:
            self.energy = 10

    def play(self):
        if self.energy >= 2:
            self.energy -= 2
        else:
            self.energy = 0

        if self.happiness <= 8:
            self.happiness += 2
        else:
            self.happiness = 10

        if self.hunger <= 9:
            self.hunger += 1
        else:
            self.hunger = 10

    def get_status(self):
        return f"The pet {self.name} has {self.hunger} hunger, {self.energy} energy and {self.happiness} happiness."

    def train(self, trick: str):
        self.tricks.append(trick)
        print(f"{self.name} is now able to {trick}.")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name}'s tricks:")
            for trick in self.tricks:
                print(f" - {trick}")
        else:
            print(f"{self.name} has not learnt any tricks yet.")
