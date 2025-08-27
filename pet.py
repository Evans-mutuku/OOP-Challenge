class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []
        print(f"🐶 Creating pet: {self.name}")

    def eat(self):
        print(f"{self.name} is eating")
        self.hunger = max(0, self.hunger - 3)
        self.happiness = max(0, min(10, self.happiness + 2))
     

    def sleep(self):
       print(f"{self.name} is sleeping")
       self.energy = min(10, self.energy + 5)

    def play(self):
        if self.energy == 0:
            print(f"{self.name} cannot play right now. {self.name} has no energy.")
            return
        else:
            print(f"{self.name} is playing")
            self.energy = max(0, self.energy - 2)
            self.happiness = max(0, min(10, self.happiness + 2))
            self.hunger = min(10, self.hunger + 1)

    def train(self, tricks):
        self.tricks.append(tricks)

    def get_status(self):
        if self.energy <= 5:
            energy_message = f"{self.name} is getting tired."
        else:
            energy_message = f"{self.name} is full of energy."
        if self.happiness <= 5:
            happiness_message = f"{self.name} is getting getting sad."
        else:
            happiness_message = f"{self.name} is happy."
        if self.hunger >= 5:
            hunger_message = f"{self.name} is getting hungry."
        else:
            hunger_message = f"{self.name} is full."
        print(f"{self.name} current status: ")
        print(f"Hunger: {self.hunger}, {hunger_message}\n Energy: {self.energy}, {energy_message}\n Happiness: {self.happiness}, {happiness_message}")
        print(f"Tricks: {self.tricks}") if len(self.tricks) > 0 else print(f"Tricks: None")
    



