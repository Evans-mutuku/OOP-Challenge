#Import the Pet class from pet.py
from pet import Pet

#Create a pet object
the_pet = Pet("Ginger" , 6 , 7 , 4)

#Teach the pet trick(s)
the_pet.train("Fetch")
the_pet.train("Roll over")

#Calling the methods of the pet object
the_pet.eat()
the_pet.sleep()
the_pet.play()

#Show the pets tricks
the_pet.show_tricks()

print(the_pet)
print(the_pet.get_status())