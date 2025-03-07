'''Write a Python program to create a class and access its properties using an object.'''

class person:
    name: str
    age: int
    def getdata(self,):
        self.name = input("Enter your name :")
        self.age = input("Enter yourage :")
        
    def printdata(self):
        print("Name is :",self.name)
        print("Age is :",self.age)
        
pr = person()
pr.getdata()
pr.printdata()