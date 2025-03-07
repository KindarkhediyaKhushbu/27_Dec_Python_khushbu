#Write a Python program to show hybrid inheritance.

class Animal:
    def speak(self):
        print("Animal makes a sound")

class Mammal(Animal):
    def walk(self):
        print("Mammal walks")


class Canine:
    def bark(self):
        print("Canine barks")


class Dog(Mammal, Canine):
    def fetch(self):
        print("Dog fetches the ball")


dog = Dog()
print("Dog's behavior:")
dog.speak()   
dog.walk()    
dog.bark()  
