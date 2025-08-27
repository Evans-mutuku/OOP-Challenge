# This is the main file that uses the Pet class from the pet module.
from pet import Pet

# Create a pet
my_pet = Pet("Tambo")
print(f"Creating pet: {my_pet.name}")

# Interact with your pet
my_pet.eat()
my_pet.play()
my_pet.sleep()
my_pet.train("roll over")
my_pet.train("play dead")
my_pet.get_status()
my_pet.show_tricks()
my_pet.get_mood()
