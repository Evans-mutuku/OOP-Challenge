class Pet:
    def __init__(self, name="Wizkid", pet_type="🐶"):
        self.name = name
        self.hunger = 10
        self.energy = 10
        self.happiness = 5
        self.pet_type = pet_type
        self.tricks = []

    def eat(self):
        old_hunger = self.hunger
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.pet_type} {self.name} is eating 🍲🍲🍲! Hunger: {old_hunger} → {self.hunger}, Happiness: +1 🥰")

    def sleep(self):
        old_energy = self.energy
        self.energy = min(10, self.energy + 5)
        print(f"{self.pet_type} {self.name} is taking a nap 😴. Energy: {old_energy} → {self.energy}")

    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.pet_type} {self.name} is playing 🎾! Energy: -2, Happiness: +2 😄, Hunger: +1")
        else:
            print(f"{self.pet_type} {self.name} is too tired to play 😓. Try letting them sleep.")

    def train(self, trick):
        if trick not in self.tricks:
            self.tricks.append(trick)
            self.happiness = min(10, self.happiness + 1)
            print(f"{self.pet_type} {self.name} learned a new trick: {trick} 🎉! Happiness +1")
        else:
            print(f"{self.pet_type} {self.name} already knows how to {trick} 😎")

    def show_tricks(self):
        if self.tricks:
            tricks_str = ', '.join(self.tricks)
            print(f"{self.pet_type} {self.name} knows the following tricks: {tricks_str}")
        else:
            print(f"{self.pet_type} {self.name} hasn't learned any tricks yet 🧐.")

    def get_status(self):
        print(f"""
--- {self.pet_type} {self.name}'s Status ---
Hunger:    {self.hunger}/10 {'🟥' if self.hunger > 7 else '🟨' if self.hunger > 4 else '🟩'}
Energy:    {self.energy}/10 {'🟩' if self.energy > 7 else '🟨' if self.energy > 4 else '🟥'}
Happiness: {self.happiness}/10 {'😃' if self.happiness > 7 else '🙂' if self.happiness > 4 else '😢'}
-----------------------------------------
""")



wizkid = Pet()  # No need to pass name; it's already "Wizkid"
wizkid.get_status()
wizkid.eat()
wizkid.train("dance like Starboy 💃")
wizkid.show_tricks()
wizkid.show_tricks()
