class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5  # Initial hunger level (range 0-10)
        self.energy = 5  # Initial energy level (range 0-10)
        self.happiness = 5  # Initial happiness level (range 0-10)
        self.tricks = []  # List to store tricks the pet learns

    def eat(self):
        """Reduces hunger by 3, increases happiness by 1."""
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} is eating. Hunger: {self.hunger}, Happiness: {self.happiness}")

    def sleep(self):
        """Increases energy by 5, max to 10."""
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} is sleeping. Energy: {self.energy}")

    def play(self):
        """Decreases energy by 2, increases happiness by 2, increases hunger by 1."""
        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)
        print(f"{self.name} is playing. Energy: {self.energy}, Happiness: {self.happiness}, Hunger: {self.hunger}")

    def get_status(self):
        """Prints current state of the pet."""
        print(f"Status of {self.name}:")
        print(f"Hunger: {self.hunger}/10, Energy: {self.energy}/10, Happiness: {self.happiness}/10")

    def train(self, trick):
        """Teaches the pet a new trick."""
        self.tricks.append(trick)
        print(f"{self.name} learned a new trick: {trick}")

    def show_tricks(self):
        """Shows all tricks the pet has learned."""
        if self.tricks:
            print(f"{self.name} knows the following tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")
