'''Write Python programs to demonstrate different types of inheritance (single, multiple, multilevel, etc.).'''

# single inheritance

'''class father:
    tractor : int
    car : int
    balance : int
    
    def getdata(self):
        self.tractor = input("Enter number of Tractor :")
        self.car =input("Enter number of car :")
        self.balance = input("Enter balance :")
    
class son(father):
    def printdata(self):
        print("Number of tractor is :",self.tractor)
        print("Number of car is :",self.car)
        print("Balance is :",self.balance)
        
       
s1 = son()
s1.getdata()
s1.printdata()'''
    
    
#Multiple Inhe

'''class person1:
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
fa.printdata()'''

#Multilavel inheritance

class creat_acc:
    account_no = int
    holder_name = str
    account_type = str
    dep_amount = int
    balance = int
    withdraw_amount = int 

    def account_create(self):
        self.account_no = int(input("Enter the account no:"))
        self.holder_name = input("Enter the holder name:")
        self.account_type = input("Enter the account type:")
        self.balance = int(input("Enter your balance:"))
        print("ACCOUNT CREATED SUCCESSFULLY")

class deposit(creat_acc):
    
    def deposit(self):
        self.dep_amount = int(input("Enter the amount to deposit:"))
        if self.dep_amount >= 2000:
            self.balance += self.dep_amount
            print("Amount deposited")
        else:
            print("Minimum deposit amount is 2000")
            
            
class withdraw(deposit):
    
    def withdraw(self):
        self.withdraw_amount = int(input("Enter the amount to withdraw:"))
        if self.withdraw_amount <= self.balance:
            self.balance -= self.withdraw_amount
            print("Amount withdrawn")
        else:
            print("Insufficient balance")
            
class bank(withdraw):
    
    def printdata(self):
        print("______________BANK INFORMATION________________")
        print("Acc no:",self.account_no)
        print("Holder name:",self.holder_name)
        print("Account Type:",self.account_type)
        print("Balance:",self.balance)
        
        
bk = bank()
bk.account_create()
bk.deposit()
bk.withdraw()
bk.printdata()


