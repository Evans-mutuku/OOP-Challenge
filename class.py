from pet import Pet

def main():
    # Creating a new pet(user interaction)
    my_pet= Pet(input("Enter the name of your pet: "))

    # Initialise pet interactions
    my_pet.eat()
    my_pet.play()
    my_pet.sleep()

    # initialising pet tricks and adding them with a value
    my_pet.train("roll over")
    my_pet.train("fetch")
 
    # Final status and tricks
    my_pet.show_tricks()
    my_pet.get_status()
  
# controlling script execution(running from main and being)
if __name__ == "__main__":
    main()
