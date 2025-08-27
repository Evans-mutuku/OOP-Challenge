from pet import Pet

# Create pet and print creation message
print("Creating pet: Luffy🐕")
my_pet = Pet("Luffy🐕")

# Perform basic actions
print("\n=== ✨ Let's take care of our pet! ===")
my_pet.eat()
my_pet.play()
my_pet.sleep()

# Train tricks
print("\n=== 🎓 Time for training! ===")
my_pet.train("Roll Over")
my_pet.train("Play Dead")
my_pet.train("Fetch")    

# Show final status
my_pet.get_status()

