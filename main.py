from pet import Pet  # Import the Pet class from the pet module

# Create an instance of the Pet class with the name "Luna"
pet = Pet("Luna")

# Display the initial status of the pet
pet.get_status()

# Perform actions on the pet
pet.eat()  # Feed the pet to reduce hunger and increase happiness
pet.sleep()  # Let the pet sleep to restore energy
pet.play()  # Play with the pet to increase happiness and reduce energy

# Display the updated status of the pet after actions
pet.get_status()

# Train the pet to learn new tricks
pet.train("Roll Over")  # Teach the pet to roll over
pet.train("Bark")  # Teach the pet to bark
pet.train("Run")  # Teach the pet to run

# Display all the tricks the pet has learned
pet.show_tricks()

