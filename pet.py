# pet.py

class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        old_hunger = self.hunger
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} is eating... 🍽️ (Hunger: {old_hunger} → {self.hunger}, Happiness +1 😊)")

    def sleep(self):
        old_energy = self.energy
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} is sleeping... 😴 (Energy: {old_energy} → {self.energy})")

    def play(self):
        if self.energy < 2:
            print(f"{self.name} is too tired to play... 💤 (Energy: {self.energy})")
            return
        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)
        print(f"{self.name} is playing... 🎾 (Energy -2, Hunger +1, Happiness +2 😄)")

    def train(self, trick):
        if trick.lower() in [t.lower() for t in self.tricks]:
            print(f"{self.name} already knows how to '{trick}'! 🙃")
        else:
            self.tricks.append(trick)
            self.happiness = min(10, self.happiness + 1)
            print(f"{self.name} learned a new trick: '{trick}'! 🎓 (Happiness +1 🐾)")

    def show_tricks(self):
        if not self.tricks:
            print(f"{self.name} hasn’t learned any tricks yet. 😢")
        else:
            print(f"{self.name}'s tricks: 🐶✨ " + ", ".join(self.tricks))

    def get_status(self):
        print(f"\n📋 {self.name}'s Current Status:")
        print(f"🍗 Hunger: {self.hunger}/10")
        print(f"⚡ Energy: {self.energy}/10")
        print(f"😊 Happiness: {self.happiness}/10")
        self.show_tricks()
        print("-" * 30)


