from pet import Pet
 
pet_name = input("🐾 What is your pet's name? ")
pet_type = input("🐶🐱🐦 What type of pet do you have?, is it a (Dog, Cat, Bird, etc.): ")

my_pet = Pet(pet_name, pet_type)
 
my_pet.get_status()
 
while True:
    action = input("🤔 What do you want your pet to do? (eat/play/sleep/train/dance/sing/status/exit): ").lower()

    if action == "eat":
        my_pet.eat()
    elif action == "play":
        my_pet.play()
    elif action == "sleep":
        my_pet.sleep()
    elif action == "train":
        trick = input("🎓 Enter a trick to teach: ")
        my_pet.train(trick)
    elif action == "dance":
        my_pet.dance()
    elif action == "sing":
        my_pet.sing()
    elif action == "status":
        my_pet.get_status()
    elif action == "exit":
        print("👋 Goodbye! See you next time! 🐾")
        break
    else:
        print("🚫 Invalid action! Try again.")
 
my_pet.get_status()
