from pet import Pet

my_pet = Pet("Gigi")

# Initial status
print(my_pet.get_status())

# First round of interactions
my_pet.eat()
my_pet.sleep()
my_pet.play()

# Teach tricks
my_pet.train("roll over")
my_pet.train("fetch")
my_pet.train("shake hands")
my_pet.train("spin")
my_pet.train("play dead")
my_pet.train("sit")
my_pet.train("jump")

# Show tricks
my_pet.show_tricks()

# Second round of interactions
my_pet.eat()
my_pet.play()
my_pet.sleep()

# Final status and tricks
print(my_pet.get_status())
my_pet.show_tricks()
