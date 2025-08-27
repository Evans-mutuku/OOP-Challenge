class Pet:
  def __init__(self,name,hunger, energy, happiness):
   self.name = name
   self.hunger = hunger
   self.energy = energy
   self.happiness = happiness

  

  
  def eat(self):
    self.hunger = max(0, self.hunger -3)
    self.happiness = min(10, self.happiness + 1)
  def sleep(self):
    self.energy += 5

  def play(self):
    self.energy -= 2
    self.happiness = min(10, self.happiness + 2)
    self.hunger += 2

  def get_status(self):
    print(f"{self.name} | Hunger: {self.hunger} | Energy:{self.energy}|  Happiness:{self.happiness}")

my_pet = Pet("cuty", 5,5,5)

my_pet.eat()
my_pet.sleep()
my_pet.play()
my_pet.get_status()