class Pet:
    def __init__(self, name, pet_type="Dog"):
        self.name = name
        self.pet_type = pet_type
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []
        self.level = 1   

    def get_mood(self):
        if self.happiness > 8:
            return "Excited 😃🎉✨"
        elif self.happiness < 3:
            return "Sad 😞💔"
        elif self.hunger > 8:
            return "Starving 🍽️🥺"
        elif self.energy < 3:
            return "Exhausted 😴💤"
        else:
            return "Content 😊🐾"

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"🍽️ {self.name} ate delicious food! Yum! 😋 (Hunger: {self.hunger}, Happiness: {self.happiness})")

    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"😴💤 {self.name} had a restful nap and feels refreshed! (Energy: {self.energy})")

    def play(self):
        if self.hunger >= 8:
            print(f"🚫 {self.name} is too hungry to play! 🍽️ Feed them first. 🥺")
        elif self.energy < 2:
            print(f"😞 {self.name} is too tired to play! Let them sleep first. 😴💤")
        else:
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"🎾🐶 {self.name} had so much fun playing! (Energy: {self.energy}, Happiness: {self.happiness}, Hunger: {self.hunger})")

    def train(self, trick):
        self.tricks.append(trick)
        self.happiness = min(10, self.happiness + 2)
        self.level += 1  # Level up when learning a trick
        print(f"🏅✨ {self.name} mastered '{trick}'! (Happiness: {self.happiness}, Level: {self.level})")

    def show_tricks(self):
        print(f"🐾🎓 {self.name} knows these tricks: {', '.join(self.tricks)}" if self.tricks else f"😥 {self.name} hasn't learned any tricks yet.")

    def dance(self):
        if self.happiness >= 8:
            print(f"💃🎉 {self.name} is showing off some cool moves! So happy!")
        else:
            print(f"😅 {self.name} doesn’t feel like dancing right now.")

    def sing(self):
        if self.pet_type.lower() == "bird":
            print(f"🎶🐦 {self.name} sings a beautiful melody! 🌿🎵")
        else:
            print(f"🚫 {self.name} can't sing, but loves to play! 🎾😊")

    def get_status(self):
        print(f"🐾 {self.name}'s Status 🐾")
        print(f"Hunger: {self.hunger}/10 🍽️ | Energy: {self.energy}/10 ⚡ | Happiness: {self.happiness}/10 😊")
        print(f"Mood: {self.get_mood()} | Level: {self.level} ⭐")
        self.show_tricks()
