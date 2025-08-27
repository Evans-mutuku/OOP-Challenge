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
        print(f"{self.name} is eating...🍽️")

    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} is sleeping...💤")

    def play(self):
        if self.energy < 2:
            print(f"{self.name} is too tired to play... 😴")
        else:
            self.energy = max(0, self.energy - 2)
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print( f"\nYaay!! {self.name} is playing... 🎾")

    def get_status(self):
        print(f"\n✨This is how {self.name}'s doing:")
        print(f"🍗Hunger: {self.hunger}")
        print(f"💤Energy: {self.energy}")
        print(f"😊Happiness: {self.happiness}")
        print(f"🎓Tricks: {self.tricks if self.tricks else 'None:('}")

    def train(self, trick):
        self.tricks.append(trick)
        self.happiness = min(10, self.happiness + 1)
        print(f"\n🎉 Guess what! {self.name} learned a new trick: {trick}!")

    def show_tricks(self):
        print(f"{self.name}'s tricks: {', '.join(self.tricks) if self.tricks else 'None yet 😢'}")

    
    # # Mood system

    def get_mood(self):
        mood_score = self.energy + self.happiness - self.hunger
    
        print(f"\n🧠 Mood check for {self.name}...")

        if mood_score >= 15:
            print("😍 Feeling fantastic!")
        elif mood_score >= 10:
            print("🙂 Doing pretty well!")
        elif mood_score >= 5:
            print("😐 Could use a snack or nap.")
        else:
            print("😞 Feeling a bit off. Maybe some love will help.")

        # Specific needs
        if self.hunger >= 8:
            print("🍗 I'm *really* hungry!")
        elif self.hunger >= 5:
            print("😋 A little snack wouldn't hurt...")

        if self.energy <= 2:
            print("😴 So... tired... must sleep.")
        elif self.energy <= 4:
            print("🥱 I'm starting to feel sleepy.")

        if self.happiness <= 2:
            print("😢 I feel lonely... can we play?")
        elif self.happiness <= 4:
            print("😐 I'm kinda bored.")





