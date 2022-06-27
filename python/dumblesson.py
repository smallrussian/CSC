from typing import Mapping


class Animal:
    def __init__(self, creature, noise):
        self.creature=creature
        self.noise=noise
    def getplace(self):
        return "farm"
    def getstatement(self):
        return "E I E I O"
class LakeAnimal(Animal):
    def getplace(self):
        return "lake"
    def getstatement(self):
        return "Glub Glub Glub"
class JParkAnimal(Animal):
    def getplace(self):
        return "Jurassic Park"
    def getstatement(self):
        return "Quickly run away"
animals=[]
Pig=Animal('Pig', 'Oink')
Cow=Animal('Cow', 'Moo')
Fish=LakeAnimal('Fish', 'bubble')
Gator=LakeAnimal('Gator', 'Chomp')
TRex=JParkAnimal('TRex', 'ROAR!')
animals.append(Pig)
animals.append(Cow)
animals.append(Fish)
animals.append(Gator)
animals.append(TRex)
for animal in animals:
    print("\nOld MacDonald had a {} {}".format(animal.getplace(), animal.getstatement()))
    print("And on that {} he had a {} {}".format(animal.getplace(), animal.creature, animal.getstatement()))
    print("With a {} {} here and a {} {} over there".format(animal.noise, animal.noise, animal.noise, animal.noise))
    print("Here a {}, there a {}, everywhere a {}{}".format(animal.noise, animal.noise, animal.noise, animal.noise))
    print("Old MacDonald had a {} {}".format(animal.getplace(), animal.getstatement()))
        