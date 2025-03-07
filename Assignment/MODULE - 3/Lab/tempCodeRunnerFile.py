class father:
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
s1.printdata()