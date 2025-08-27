class Pet:
    # Constructor to initialize the pet's attributes
    def __init__(self, name):
        self.name = name  # Name of the pet
        self.hunger = 15  # Hunger level (higher means hungrier)
        self.energy = 10  # Energy level
        self.happiness = 20  # Happiness level
        self.tricks = []  # List of tricks the pet knows

    def eat(self):
        pass

    def sleep(self):
        pass

    def play(self):
        pass

    def train(self, trick):
        pass

    def show_tricks(self):
        if self.tricks:  # Check if the pet knows any tricks
            print(f"{self.name} knows these tricks: {', '.join(self.tricks)}")  # List the tricks
        else:
            print(f"{self.name} knows zero tricks at the moment.")  # Notify if no tricks are known

    def get_status(self):
        pass

