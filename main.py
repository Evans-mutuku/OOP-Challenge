# main.py

from pet import Pet

# Create a pet object named Max
print("🐾 Creating pet: Rex 🐾")
my_pet = Pet("Rex")

# Call methods to simulate actions
print("🍽️ Rex is eating...")
my_pet.eat()
print("🎾 Rex is playing...")
my_pet.play()
print("🛌 Rex is sleeping...")
my_pet.sleep()

# Train the pet with predefined tricks
print("🐕‍🦺 Rex is learning tricks...")
my_pet.train("roll over")
my_pet.train("play dead")
my_pet.train("fetch")
my_pet.train("sit")
my_pet.train("do the monkey dance")    
my_pet.train("jump")
my_pet.train("spin")    
my_pet.train("high five")
my_pet.train("shake hands")

# Display the pet's current status and tricks
print("📋 Rex's current status:")
print(f"🍗 Hunger: {my_pet.hunger}")
print(f"⚡ Energy: {my_pet.energy}")
print(f"😄 Happiness: {my_pet.happiness}")
print(f"🎩 Tricks: {my_pet.tricks}")
my_pet.show_tricks()
print("🐾 Rex's status:")