from pet import Pet

def main():
    print("Creating pet: Max")
    pet = Pet("Max")
    
    # Test basic functionality
    pet.eat()
    pet.play()
    pet.sleep()
    
    # Test training
    pet.train("roll over")
    pet.train("play dead")
    
    # Show status
    pet.get_status()
    
    # Show tricks separately
    pet.show_tricks()
    
    # Test edge cases
    print("\nTesting edge cases:")
    pet.energy = 1
    pet.play()  # Should be too tired after this
    pet.play()  # Should refuse
    pet.train("sit")  # Should refuse (not enough energy)

if __name__ == "__main__":
    main()