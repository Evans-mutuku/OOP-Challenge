class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        # Check if hunger is already at max
        if self.hunger >= 10:
            print(f"{self.name} is not hungry.")
            return
        # Decrease hunger and increase energy and happiness
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)

    def sleep(self):
        #increase energy and decrease hunger and ensure it doesn't exceed max 10
        self.energy = min(10, self.energy + 5)
        self.happiness = max(0, self.happiness - 1)

     
    def play(self):
        # decrease energy and increase happiness and hunger
        # Check if energy is 0
        if self.energy <= 0:
            print(f"{self.name} is too tired to play.")
            return
        self.energy = max(0, self.energy - 3) # decrease energy
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)

    def train(self, trick):
        # increase happiness and add trick to the list of tricks
        self.happiness = min(10, self.happiness + 3)
        self.tricks.append(trick) #add trick to the list of tricks

    def show_tricks(self):
        # print the list of tricks
        if self.tricks:
            print(f"{self.name} can do the following tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} has not learned any tricks yet.")

    def get_status(self):
        # return the current status of the pet
        #print the current status of the pet
        return f"{self.name}'s status: Hunger: {self.hunger}, Energy: {self.energy}, Happiness: {self.happiness}"
        print(f"{self.name}'s learned tricks: {', '.join(self.tricks)}")
    

