#Create a program that includes animals or vehicles with the same action (like move()). However, make each class define move() differently (for example, Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️).

class Dog:
    def __init__(self,  species, age):        
        self.species = species
        self.age = age

    def move(self, movement):      
        print(f"My dog, a {self.species}, aged {self.age} moves by {movement}")      
 
class Horse:
    def __init__(self, species, age):        
        self.species = species
        self.age = age

    def move(self, movement):      
        print(f"{self.species} Horse aged {self.age} moves by {movement}")  

DogInfo = Dog("Retriver", 12)  
DogInfo.move("Running")

HorseInfo =Horse("Mustang", 15)
HorseInfo.move("Galloping")

#ouput
#My dog, a Retriver ,aged 12 moves by Running
#Mustang Horse aged 15 moves by Galloping




             