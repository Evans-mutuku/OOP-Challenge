from pet import Pet

def main():
    pet = Pet("Buddy")

    pet.get_status()

    pet.eat()
    pet.play()
    pet.sleep()

    pet.train("sit")
    pet.train("roll over")

    pet.get_status()
    pet.show_tricks()

if __name__ == "__main__":
    main()
