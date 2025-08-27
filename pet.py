class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    # Feed the pet to reduce hunger and increase happiness
    def eat(self):
        print(f"🍽️{self.name} is eating...")
        self.hunger = max(self.hunger - 3, 0)
        self.happiness = min(self.happiness + 1, 10)

    # Let the pet sleep to restore energy
    def sleep(self):
        print(f"😴{self.name} is sleeping...💤")
        self.energy = min(self.energy + 5, 10)
    
    # Play with pet to increase happiness but consume energy
    def play(self):
        print(f"🎾{self.name} is playing...🎯")
        self.energy = max(self.energy - 2, 0)
        self.happiness = min(self.happiness + 2, 10)
        self.hunger = min(self.hunger + 1, 10)

     # Teach the pet a new trick if it has enough energy
    def train(self, trick):
        if self.energy >= 2:
            self.tricks.append(trick.lower())
            self.energy -= 2
            self.happiness = min(self.happiness + 1, 10)
        else:
            print(f"😫{self.name} is too tired to train!")

    # Display all current stats of the pet
    def get_status(self):
        print(f"\n{self.name}'s current status:")
        print(f"🍖Hunger: {self.hunger}")
        print(f"⚡Energy: {self.energy}")
        print(f"💖Happiness: {self.happiness}")
        print(f"🎯Tricks: {self.tricks}")
