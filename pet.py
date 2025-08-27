class Pet:
    # Constructor to initialize the pet's attributes
    def __init__(self, name):
        self.name = name  # Name of the pet
        self.hunger = 15  # Hunger level (higher means hungrier)
        self.energy = 10  # Energy level
        self.happiness = 20  # Happiness level
        self.tricks = []  # List of tricks the pet knows

    def eat(self):
         #Reduces hunger by 3 points (but not below 0),and increases happiness by 1 (capped at 100).
        
        if self.hunger == 0:
            print(f"{self.name} is not hungry right now!")
        else:
            self.hunger = max(0, self.hunger - 3)
            self.happiness = min(100, self.happiness + 1)
            print(f"{self.name} has eaten. Hunger: {self.hunger}, Happiness: {self.happiness}")

    def sleep(self):
        pass

    def play(self):
        pass

    def train(self, trick):
        pass

    def show_tricks(self):
        pass

    def get_status(self):
        pass

