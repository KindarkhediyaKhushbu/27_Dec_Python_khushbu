# Write a Python program to show multiple inheritance.


class person1:
    id: int
    name: str
    age: int
    sub: str
    
    def per_getdata1(self):
        self.sd = input("Enter Person1 ID:")
        self.name = input("Enter person1 name:")
        self.age = input("Enter person1 age:")
        self.sub = input("Enter perso1 subject:")


class person2:
    id: int
    name: str
    age: int
    sub: str
    
    def per_getdata2(self):
        self.sd = input("Enter Person2 ID:")
        self.name = input("Enter person2 name:")
        self.age = input("Enter person2 age:")
        self.sub = input("Enter person2 subject:")

class person3:
    id: int
    name: str
    age: int
    sub: str
    
    def per_getdata3(self):
        self.sd = input("Enter Person3 ID:")
        self.name = input("Enter person3 name:")
        self.age = input("Enter person3 age:")
        self.sub = input("Enter person3 subject:")


class father(person1,person2,person3):
    def printdata(self):
        print("-----------PERSON1 INFORMATION-----------")
        print("Person1 id is:", self.id)
        print("Person1 name is :", self.name)
        print("Person1 age is :",self.age)
        print("person1 subject is :",self.sub)
        

        print("-----------PERSON2 INFORMATION-----------")
        print("Person1 id is:", self.id)
        print("Person1 name is :", self.name)
        print("Person1 age is :",self.age)
        print("person1 subject is :",self.sub)
        
        
        print("-----------PERSON3 INFORMATION-----------")
        print("Person1 id is:", self.id)
        print("Person1 name is :", self.name)
        print("Person1 age is :",self.age)
        print("person1 subject is :",self.sub)
        


fa = father ()
fa.per_getdata1()
fa.per_getdata2()
fa.per_getdata3()
fa.printdata()