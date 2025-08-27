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
        self.tricks.append(trick)  # Add the new trick to the list of tricks
        print(f"{self.name} learned a new trick: {trick}!")  # Notify the user


    def show_tricks(self):
        pass

    def get_status(self):
        pass

