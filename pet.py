class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        self.hunger = max(self.hunger - 3, 0)
        self.happiness = min(self.happiness + 1, 10)
        print(f"{self.name} had a meal. 🍽️")

    def sleep(self):
        self.energy = min(self.energy + 5, 10)
        print(f"{self.name} took a nap. 😴")

    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(self.happiness + 2, 10)
            self.hunger = min(self.hunger + 1, 10)
            print(f"{self.name} played and had fun! 🐾")
        else:
            print(f"{self.name} is too tired to play. 😩")

    def get_status(self):
        print(f"🐶 {self.name}'s Status:")
        print(f"  Hunger: {self.hunger}/10")
        print(f"  Energy: {self.energy}/10")
        print(f"  Happiness: {self.happiness}/10")

    def train(self, trick):
        self.tricks.append(trick)
        self.happiness = min(self.happiness + 1, 10)
        print(f"{self.name} learned a new trick: {trick}! 🎉")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows these tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet. 🐾")


# Example usage:
# Create a new pet named "Buddy"
buddy = Pet("Buddy")

buddy.get_status()
buddy.eat()
buddy.sleep()
buddy.play()
buddy.train("roll over")
buddy.show_tricks()
buddy.get_status()

