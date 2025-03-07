#Write a Python program to show hierarchical inheritance.
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")


class Cat(Animal):
    def meow(self):
        print("Cat meows")


class Cow(Animal):
    def moo(self):
        print("Cow moos")


dog = Dog()
cat = Cat()
cow = Cow()


print("Dog behavior:")
dog.speak()  
dog.bark()   

print("\nCat behavior:")
cat.speak()  
cat.meow()  

print("\nCow behavior:")
cow.speak()  
cow.moo()    
