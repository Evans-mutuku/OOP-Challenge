# 🐶 Python OOP Challenge: Build Your Own Digital Pet

Welcome to this week's Python challenge! 🎉

In this challenge, you’ll be creating a virtual pet using Object-Oriented Programming concepts in Python. This fun project will help you practice how to use classes, attributes, methods, and constructors.

---

## 🧠 Objective

Create a class called `Pet` with the following:

### Attributes:
- `name`: the name of your pet
- `hunger`: an integer representing hunger level (0 = full, 10 = very hungry)
- `energy`: an integer representing energy level (0 = tired, 10 = fully rested)
- `happiness`: an integer (0–10)

### Methods:
- `eat()`: reduces hunger by 3 points (but not below 0), and increases happiness by 1.
- `sleep()`: increases energy by 5 points (but not above 10).
- `play()`: decreases energy by 2, increases happiness by 2, and increases hunger by 1.
- `get_status()`: prints the current state of the pet.

### Bonus 🎯
- Add a method `train(trick)` that teaches your pet a new trick and stores it in a list.
- Add a method `show_tricks()` that prints all learned tricks.

---

## 📝 How to Complete

1. Fork or clone this repo.
2. Write your `Pet` class in `pet.py`.
3. In `main.py`, create a pet object and call its methods to test functionality.
4. Submit a GitHub repo or a zipped folder with your code and a screenshot of the output.

---

Tricks: ['roll over', 'play dead']


### 💡 Tips
Use max() and min() to keep values between 0 and 10.

Think about edge cases like trying to play when energy is 0.

🏁 Submission

Submission format: clone/fork this repo

Bonus points for creativity (custom actions, emojis, pet types, etc.)
class VirtualPet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5      # 0 = full, 10 = very hungry
        self.energy = 5      # 0 = tired, 10 = fully rested
        self.happiness = 5   # 0 = sad, 10 = very happy
        self.tricks = []     # list of tricks the pet has learned

    def eat(self):
        old_hunger = self.hunger
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} ate some food. Hunger: {old_hunger} → {self.hunger}, Happiness: +1")

    def sleep(self):
        old_energy = self.energy
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} slept well. Energy: {old_energy} → {self.energy}")

    def play(self):
        if self.energy >= 2:
            self.energy = max(0, self.energy - 2)
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.name} played and had fun! Energy: -2, Happiness: +2, Hunger: +1")
        else:
            print(f"{self.name} is too tired to play.")

    def train(self, trick):
        if trick not in self.tricks:
            self.tricks.append(trick)
            print(f"{self.name} learned a new trick: {trick}!")
        else:
            print(f"{self.name} already knows how to {trick}.")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows the following tricks:")
            for trick in self.tricks:
                print(f"- {trick}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")

    def get_status(self):
        print(f"--- {self.name}'s Status ---")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")
