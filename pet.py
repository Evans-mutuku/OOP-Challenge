# create a class pet
class Pet:
    def __init__(self, name, hunger, energy, happiness, trick):
        self.name = name
        self.hunger = hunger
        self.energy = energy
        self.happiness = happiness
        self.trick = trick
        self.trick_learned = []  # Initialize an empty list to store learned tricks

        print("Let's play a game.")

        # enquire for attributes
        name = input("What is your pet's name? ")
        print(f"Creatng pet {name}...")

    def eat(self):
        self.hunger = int(input("How hungry is your pet? (0 - full, 10 - very hungry) "))

        if self.hunger < 5:
            print(f"{self.name} is not hungry.")
            return
        elif self.hunger >= 6:
            print(f"{self.name} is starving!")
            print(f"{self.name} is eating.")
            return 

        # when eating(), it reduces hunger by 3 points and increases happiness by 1 point
        self.hunger -= 3
        self.happiness += 1

        if self.happiness > 10:
            self.happiness = 10

    def sleep(self):
        self.energy = int(input("How energetic is your pet? (Min(0), Max(10)) "))

        if self.energy >= 6:
            print(f"{self.name} is so energetic.")
            return
        elif self.energy <= 5:
            print(f"{self.name} is exhausted!")
            print(f"{self.name} is sleeping.")
            return

        # when sleeping(), it increases energy by 5 points but not above 10
        self.energy += 5

        if self.energy > 10:
            self.energy = 10

    def play(self):
        self.happiness = int(input("How happy is your pet? (Min(0), Max(10)) "))

        if self.happiness >= 6:
            print(f"{self.name} is playing.")
            return
        elif self.happiness <= 5:
            print(f"{self.name} is sad!")
            return
        
        # when playing(), it reduces energy by 2 points and increases happiness by 2 points and increases hunger by 1 points
        self.energy -= 2
        self.happiness += 2
        self.hunger += 1

        if self.energy < 0:
            self.energy = 0

        if self.happiness > 10:
            self.happiness = 10

        if self.hunger > 10:
            self.hunger = 10

    # print the current state of the pet
    def get_status(self):
        print(f"Current status of {self.name}:")
        print(f"Name: {self.name}")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Happiness: {self.happiness}")

    def train(self, trick):
        self.trick = trick 
        trick = input("What trick do you want to train your pet? (e.g., sit, roll over) ")
        print(f"Training {self.name} to do the trick: {trick}")
        print(f"Your pet has learned a new trick: {trick}")
        self.trick_learned.append(trick)  # Add the trick to the list of learned tricks
        return self.trick_learned
    
    # prints all learned tricks
    def show_tricks(self):
        print(f"Your pet has learned the following tricks: {self.trick_learned}")
        return self.trick_learned
