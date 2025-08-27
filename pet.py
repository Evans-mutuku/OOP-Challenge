class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []
    
    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} is eating... 🍖")
    
    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} is sleeping... 💤")
    
    def play(self):
        if self.energy <= 0:
            print(f"{self.name} is too tired to play! 😴")
            return
        
        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)
        print(f"{self.name} is playing... 🎾")
    
    def get_status(self):
        print(f"\n{self.name}'s current status:")
        print(f"Hunger: {self.hunger} {'🍽️' * (10 - self.hunger)}")
        print(f"Energy: {self.energy} {'⚡' * self.energy}")
        print(f"Happiness: {self.happiness} {'❤️' * self.happiness}")
        if self.tricks:
            print(f"Tricks: {self.tricks}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")
    
    def train(self, trick):
        if self.energy < 3:
            print(f"{self.name} is too tired to learn new tricks! 😫")
            return
        
        self.energy = max(0, self.energy - 3)
        self.hunger = min(10, self.hunger + 2)
        self.tricks.append(trick)
        print(f"🎉 {self.name} learned a new trick: {trick}!")
    
    def show_tricks(self):
        if not self.tricks:
            print(f"{self.name} hasn't learned any tricks yet. 😢")
        else:
            print(f"{self.name} knows these tricks:")
            for i, trick in enumerate(self.tricks, 1):
                print(f"{i}. {trick}")